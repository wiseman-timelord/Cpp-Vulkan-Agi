# .\scripts\menu-display.py

import gradio as gr

def chatbot_response(agent, tokenizer, device, user_input, chat_history):
    prompt = "You are a helpful assistant."
    messages = [{"role": "system", "content": prompt}] + [{'role': 'user', 'content': msg[0]} for msg in chat_history]
    messages.append({'role': 'user', 'content': user_input})
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    generated_ids = agent.generate(model_inputs.input_ids, max_new_tokens=512)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    chat_history.append((user_input, response))
    return chat_history

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
                    lambda agent_type, user_input, chat_history: chatbot_response(agents[agent_type], tokenizer, device, user_input, chat_history),
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
