# .\scripts\model_interaction.py - for interaction with the models.

import subprocess
from scripts.utility_script import monitor_resources, manage_models_in_gpu, manage_models_in_ram
from scripts.prompt_utils import prompt_response, initialize_model, parse_agent_response, read_and_format_prompt



def run_llama_cli(cpp_binary_path, model_path, prompt=None, max_memory_usage=None, use_gpu=True):
    command = [
        cpp_binary_path,
        "-m", model_path,
        "-c", "512",
        "-b", "1024",
        "-n", "256",
        "--keep", "48",
        "--repeat_penalty", "1.0",
        "--color",
        "-i",
        "-r", "User:",
    ]
    if prompt:
        command.append("-p")
        command.append(prompt)

    while True:
        success, usage = monitor_resources(max_memory_usage, use_gpu)
        if not success:
            print(f"The maximum memory allowance was exceeded, model un-loaded!")
            manage_models_in_gpu(unload=True)
            return f"The maximum memory allowance was exceeded, model un-loaded! (Usage: {usage}%)"
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error running llama CLI: {e}")
            return None

def generate_response(cpp_binary_path, model_path, user_input, chat_history, max_memory_usage, use_gpu=True):
    # Ensure models are managed properly
    success, usage = monitor_resources(max_memory_usage, use_gpu)
    if not success:
        print(f"Memory usage exceeded: {usage}%, unloading models!")
        manage_models_in_ram(unload=True)
        manage_models_in_gpu(unload=True)
        return f"Memory usage exceeded: {usage}%, unloading models!"

    # Read and format the prompt
    data = utility.read_yaml()
    task_name = "converse"
    agent_type = "chat"
    prompt_file = f"./data/prompts/{task_name}.txt"
    syntax_key = f'syntax_type_{1 if agent_type == "chat" else 2}'
    formatted_prompt = read_and_format_prompt(prompt_file, data, agent_type, task_name, data[syntax_key])

    # Generate response
    max_tokens_for_task = 100
    raw_agent_response = llm(
        formatted_prompt, 
        stop=["Q:", "### Human:", "### User:"], 
        echo=False, 
        temperature=0.7, 
        max_tokens=max_tokens_for_task
    )["choices"][0]["text"]

    # Parse response
    parsed_response = parse_agent_response(raw_agent_response, data)
    return parsed_response