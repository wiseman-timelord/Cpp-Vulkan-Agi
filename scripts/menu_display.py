# .\scripts\menu-display.py

import gradio as gr
from scripts.model_interaction import generate_response

def display_task_management(agent_type, tasks):
    task_overview = f"Agent: {agent_type}\nTasks:\n"
    for task in tasks:
        task_overview += f"- {task}\n"
    return task_overview

def setup_gradio_interface(agents, tokenizer, device):
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(height=500)
                user_input = gr.Textbox(show_label=False, placeholder="Type your message here...").style(container=False)
                submit_btn = gr.Button("Send")
                agent_selector = gr.Dropdown(choices=list(agents.keys()), label="Select Agent", value='Manager')
                submit_btn.click(
                    lambda agent_type, user_input, chat_history: generate_response(agents[agent_type], tokenizer, device, user_input, chat_history),
                    [agent_selector, user_input, chatbot], chatbot
                )
            with gr.Column(scale=1):
                task_management = gr.Markdown(value="No tasks yet.")
                submit_btn.click(
                    lambda agent_type: display_task_management(agent_type, ["Task 1", "Task 2"]),
                    agent_selector, task_management
                )
    return demo

def launch_gradio_interface(agents, tokenizer, device):
    demo = setup_gradio_interface(agents, tokenizer, device)
    demo.launch()
