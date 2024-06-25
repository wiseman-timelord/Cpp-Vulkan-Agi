# .\scripts\gradio_interface.py - for, gradio and interface, code.

import gradio as gr
from scripts.utility_script import load_config, save_config, manage_models_in_ram, manage_models_in_gpu, monitor_resources
from scripts.model_interaction import generate_response

def setup_gradio_interface():
    config = load_config('./data/config_general.json')

    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(height=500)
                user_input = gr.Textbox(show_label=False, placeholder="Type your message here...").style(container=False)
                submit_btn = gr.Button("Send")
                agent_selector = gr.Dropdown(choices=["Chat", "Instruct", "Code"], label="Select Agent", value='Chat')
                submit_btn.click(
                    lambda agent_type, user_input, chat_history: generate_response(
                        "./libraries/llama-bin-win-vulkan-x64/llama-cli.exe",
                        config[f"{agent_type.lower()}_model_used"],
                        user_input,
                        chat_history,
                        config["maximum_memory_usage"],
                        use_gpu=True
                    ),
                    [agent_selector, user_input, chatbot], chatbot
                )

            with gr.Column(scale=1):
                settings_btn = gr.Button("Settings")
                settings_output = gr.Markdown(value="")

                with gr.Accordion("Settings", open=False) as settings_menu:
                    chat_model_input = gr.Textbox(label="Chat Model Path", value=config["chat_model_used"])
                    instruct_model_input = gr.Textbox(label="Instruct Model Path", value=config["instruct_model_used"])
                    code_model_input = gr.Textbox(label="Code Model Path", value=config["code_model_used"])
                    max_memory_slider = gr.Slider(1, 99, step=1, label="Maximum Memory Usage", value=config["maximum_memory_usage"])
                    save_settings_btn = gr.Button("Save Settings")

                    save_settings_btn.click(
                        lambda chat_model, instruct_model, code_model, max_memory: save_config(
                            {"chat_model_used": chat_model, "instruct_model_used": instruct_model, "code_model_used": code_model},
                            max_memory
                        ),
                        [chat_model_input, instruct_model_input, code_model_input, max_memory_slider],
                        settings_output
                    )

                settings_btn.click(lambda: "", [], settings_output)

            with gr.Column(scale=1):
                load_btn = gr.Button("Load and Start")
                unload_btn = gr.Button("Unload")

                models = []

                load_btn.click(
                    lambda: models.extend(manage_models_in_ram([config["chat_model_used"], config["instruct_model_used"], config["code_model_used"]])),
                    [], settings_output
                )
                unload_btn.click(lambda: manage_models_in_ram(models, unload=True), [], settings_output)

    return demo

def launch_gradio_interface():
    demo = setup_gradio_interface()
    demo.launch()

if __name__ == "__main__":
    launch_gradio_interface()
