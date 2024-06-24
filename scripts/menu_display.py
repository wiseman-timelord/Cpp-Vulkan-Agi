import gradio as gr
from scripts.utility_general import load_config_wrapper, save_config_wrapper, get_system_stats
from scripts.model_interaction import generate_response

def display_task_management(agent_type, tasks):
    task_overview = f"Agent: {agent_type}\nTasks:\n"
    for task in tasks:
        task_overview += f"- {task}\n"
    return task_overview

def setup_gradio_interface(agents, cpp_binary_path, max_memory_usage):
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(height=500)
                user_input = gr.Textbox(show_label=False, placeholder="Type your message here...").style(container=False)
                submit_btn = gr.Button("Send")
                agent_selector = gr.Dropdown(choices=list(agents.keys()), label="Select Agent", value='Manager')
                submit_btn.click(
                    lambda agent_type, user_input, chat_history: generate_response(cpp_binary_path, agents[agent_type], user_input, chat_history, max_memory_usage, use_gpu='vulkan' in cpp_binary_path),
                    [agent_selector, user_input, chatbot], chatbot
                )
            with gr.Column(scale=1):
                task_management = gr.Markdown(value="No tasks yet.")
                submit_btn.click(
                    lambda agent_type: display_task_management(agent_type, ["Task 1", "Task 2"]),
                    agent_selector, task_management
                )
            with gr.Column(scale=1):
                stats_display = gr.Markdown(value="Fetching system stats...")
                def update_stats():
                    cpu_usage, memory_used, memory_total = get_system_stats()
                    return f"CPU Usage: {cpu_usage}%\nSystem Memory Used: {memory_used:.2f}GB/{memory_total:.2f}GB"
                stats_btn = gr.Button("Update Stats")
                stats_btn.click(update_stats, [], stats_display)

            # Settings section
            with gr.Column(scale=1):
                settings_btn = gr.Button("Settings")
                settings_output = gr.Markdown(value="")
                current_model, processing_method, max_memory_usage = load_config_wrapper()
                with gr.Accordion("Settings", open=False) as settings_menu:
                    model_input = gr.Textbox(label="Model Used", value=current_model)
                    processing_method_dropdown = gr.Dropdown(choices=["AVX", "AVX2", "AVX512", "OpenBlas", "Vulkan"], label="Processing Method", value=processing_method)
                    max_memory_slider = gr.Slider(1, 99, step=1, label="Maximum Load", value=max_memory_usage)
                    save_settings_btn = gr.Button("Save Settings")
                    save_settings_btn.click(
                        save_config_wrapper,
                        [model_input, processing_method_dropdown, max_memory_slider],
                        settings_output
                    )
                settings_btn.click(lambda: "", [], settings_output)

    return demo

def launch_gradio_interface(agents, cpp_binary_path, max_memory_usage):
    demo = setup_gradio_interface(agents, cpp_binary_path, max_memory_usage)
    demo.launch()
