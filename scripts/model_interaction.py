# .\scripts\model_interaction.py

import subprocess

def run_llama_cli(cpp_binary_path, model_path, prompt, gpu_memory_percentage):
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
        "-p", prompt
    ]
    if gpu_memory_percentage:
        command += ["--gpu-memory", str(gpu_memory_percentage)]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running llama CLI: {e}")
        return None

def generate_response(cpp_binary_path, agent, user_input, chat_history, max_memory_usage, use_gpu=True):
    prompt = "You are a helpful assistant.\n" + "\n".join([f"User: {msg[0]}\nAgent: {msg[1]}" for msg in chat_history]) + f"\nUser: {user_input}"
    
    response = run_llama_cli(cpp_binary_path, agent, prompt, max_memory_usage, use_gpu)
    if response:
        chat_history.append((user_input, response.strip()))
    else:
        chat_history.append((user_input, "Failed to generate response."))
    return chat_history