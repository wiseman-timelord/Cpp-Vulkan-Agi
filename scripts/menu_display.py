# .\scripts\menu-display.py

import gradio as gr
from scripts.model_interaction import generate_response
import psutil

def display_task_management(agent_type, tasks):
    task_overview = f"Agent: {agent_type}\nTasks:\n"
    for task in tasks:
        task_overview += f"- {task}\n"
    return task_overview

def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_used = memory.used / (1024 ** 3)
    memory_total = memory.total / (1024 ** 3)
    return cpu_usage, memory_used, memory_total

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
                
    return demo

def launch_gradio_interface(agents, cpp_binary_path, max_memory_usage):
    demo = setup_gradio_interface(agents, cpp_binary_path, max_memory_usage)
    demo.launch()