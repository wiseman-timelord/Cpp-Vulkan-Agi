# .\scripts\gradio_interface.py

import gradio as gr
import webbrowser
from threading import Timer
import os
import sys
import logging
from scripts.utilities_misc import handle_config, manage_models_in_ram, monitor_resources, get_vulkan_instance, get_physical_device, get_logical_device
from scripts.model_interact import generate_response
import data.configure_temporary as config_temp
import scripts.prompt_matrix as prompt_matrix
import psutil  # Import psutil to handle memory usage

# Initialize logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def get_total_vram():
    import vulkan as vk
    
    instance = get_vulkan_instance()
    physical_device = get_physical_device(instance)
    memory_properties = vk.vkGetPhysicalDeviceMemoryProperties(physical_device)
    memory_heaps = memory_properties.memoryHeaps
    total_vram = sum(heap.size for heap in memory_heaps if heap.flags & vk.VK_MEMORY_HEAP_DEVICE_LOCAL_BIT)
    return total_vram

def setup_gradio_interface():
    try:
        logger.debug("Loading configuration...")
        config = handle_config('load', './data/configure_persistent.json')

        def update_chat(user_input, chat_history):
            task_details = {
                "roles": "Chat and User Interaction",
                "description": user_input,
                "instructions": "Provide a helpful and concise response."
            }
            prompt = prompt_matrix.generate_dynamic_prompt("AI-CHAT", "chatting", task_details)
            
            response = generate_response(
                "./libraries/llama-bin-win-vulkan-x64/llama-cli.exe",
                config_temp.chat_model,
                prompt,
                chat_history,
                config_temp.max_memory_usage,
                use_gpu=True
            )
            chat_history.append((user_input, response))
            return chat_history, response

        def load_models():
            save_settings()
            manage_models_in_ram([config_temp.chat_model, config_temp.instruct_model, config_temp.code_model])
            return "Models loaded to RAM."

        def unload_models():
            save_settings()
            manage_models_in_ram([], unload=True)
            return "Models unloaded from RAM."

        def restart_and_reload():
            try:
                save_settings()
                unload_models()
                os.execv(sys.executable, ['python'] + sys.argv)
            except Exception as e:
                logger.error(f"Failed to restart and reload: {e}")

        def save_settings():
            handle_config(
                "save",
                './data/configure_persistent.json',
                {
                    "chat_model_used": config_temp.chat_model,
                    "instruct_model_used": config_temp.instruct_model,
                    "code_model_used": config_temp.code_model,
                    "maximum_memory_usage": config_temp.max_memory_usage
                }
            )
            return "Configuration saved!"

        def update_model_path(file):
            return file.name

        def get_project_plan():
            return config_temp.project_planner["current_project_plan"]

        def get_current_task():
            return config_temp.project_planner["current_task_assigned"]

        def update_memory_bars(progress=gr.Progress()):
            total_sram = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
            sram_usage_gb = psutil.virtual_memory().used / (1024 ** 3)  # Convert bytes to GB
            progress(0.5, "Updating VRAM Usage")
            total_vram = get_total_vram() / (1024 ** 3)  # Convert bytes to GB
            success, vram_usage = monitor_resources(config_temp.max_memory_usage, use_gpu=True)
            vram_usage_gb = (vram_usage / 100) * total_vram  # Convert percentage to GB
            return (f"{sram_usage_gb:.2f} GB", 
                    f"{total_sram:.2f} GB", 
                    f"{vram_usage_gb:.2f} GB", 
                    f"{total_vram:.2f} GB")

        logger.debug("Setting up Gradio interface...")
        with gr.Blocks(theme=gr.themes.Default()) as demo:
            with gr.Tabs():
                with gr.Tab("Main Page"):
                    with gr.Row():
                        # First Column
                        with gr.Column(scale=5):
                            humanoid_log = gr.Chatbot(label="HUMANOID", height=310)
                            ai_chat_log = gr.Chatbot(label="AI-CHAT", height=310)

                        # Second Column
                        with gr.Column(scale=2):
                            ai_inst_log = gr.Chatbot(label="AI-INST", height=310)
                            ai_code_log = gr.Chatbot(label="AI-CODE", height=310)

                        # Third Column
                        with gr.Column(scale=3):
                            with gr.Row():
                                project_plan = gr.Textbox(label="Project Plan", value=get_project_plan(), lines=18, interactive=False)
                            with gr.Row():
                                current_task = gr.Textbox(label="Current Task", value=get_current_task(), lines=5, interactive=False)

                    # Row for chat input
                    with gr.Row():
                        user_input = gr.Textbox(show_label=False, placeholder="Type your message here...", lines=3, scale=3)
                        submit_btn = gr.Button("Send", scale=1)
                        submit_btn.click(update_chat, [user_input, humanoid_log], [humanoid_log, ai_chat_log])

                    # Row for buttons
                    with gr.Row():
                        load_btn = gr.Button("Load Models And Start")
                        unload_btn = gr.Button("Unload Models And Shutdown")
                        restart_btn = gr.Button("Restart and Reload")
                        load_btn.click(load_models, [], None)
                        unload_btn.click(unload_models, [], None)
                        restart_btn.click(restart_and_reload, [], None)

                with gr.Tab("Models Page"):
                    with gr.Column():
                        with gr.Row():
                            chat_model_input = gr.Textbox(label="Chat Model Path:", value=config_temp.chat_model, interactive=True, lines=5, scale=3)
                            chat_model_browse = gr.File(label="Browse For Models...", file_types=['.gguf'], interactive=True, scale=1)
                            chat_model_browse.change(lambda file: setattr(config_temp, 'chat_model', update_model_path(file)), [chat_model_browse], [chat_model_input])

                        with gr.Row():
                            instruct_model_input = gr.Textbox(label="Instruct Model Path:", value=config_temp.instruct_model, interactive=True, lines=5, scale=3)
                            instruct_model_browse = gr.File(label="Browse For Models...", file_types=['.gguf'], interactive=True, scale=1)
                            instruct_model_browse.change(lambda file: setattr(config_temp, 'instruct_model', update_model_path(file)), [instruct_model_browse], [instruct_model_input])

                        with gr.Row():
                            code_model_input = gr.Textbox(label="Code Model Path:", value=config_temp.code_model, interactive=True, lines=5, scale=3)
                            code_model_browse = gr.File(label="Browse For Models...", file_types=['.gguf'], interactive=True, scale=1)
                            code_model_browse.change(lambda file: setattr(config_temp, 'code_model', update_model_path(file)), [code_model_browse], [code_model_input])

                with gr.Tab("Memory Page"):
                    with gr.Column():
                        with gr.Row():
                            sram_usage_bar = gr.Textbox(label="SRam Usage:", interactive=False)
                            sram_total_bar = gr.Textbox(label="SRam Total:", interactive=False)
                        with gr.Row():
                            vram_usage_bar = gr.Textbox(label="VRam Usage:", interactive=False)
                            vram_total_bar = gr.Textbox(label="VRam Total:", interactive=False)
                        max_memory_slider = gr.Slider(1, 99, step=1, label="Maximum Memory Usage:", value=config_temp.max_memory_usage, interactive=True)
                        max_memory_slider.change(lambda val: setattr(config_temp, 'max_memory_usage', val), [max_memory_slider], None)
                        memory_refresh_btn = gr.Button("Refresh Memory Usage")
                        memory_refresh_btn.click(update_memory_bars, [], [sram_usage_bar, sram_total_bar, vram_usage_bar, vram_total_bar])

        return demo
    except Exception as e:
        logger.error(f"Error setting up Gradio interface: {e}")
        return None

def launch_gradio_interface():
    try:
        demo = setup_gradio_interface()
        if demo is None:
            raise RuntimeError("Failed to set up Gradio interface.")
        port = 7860
        url = f"http://localhost:{port}"
        Timer(1, lambda: webbrowser.open(url)).start()
        demo.launch(server_name="localhost", server_port=port)
    except Exception as e:
        logger.error(f"Failed to launch Gradio interface: {e}")

if __name__ == "__main__":
    launch_gradio_interface()
