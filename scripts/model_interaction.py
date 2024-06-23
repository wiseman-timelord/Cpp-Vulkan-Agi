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

    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def generate_response(cpp_binary_path, agent, user_input, chat_history, gpu_memory_percentage):
    prompt = "You are a helpful assistant.\n" + "\n".join([msg[0] for msg in chat_history]) + f"\n{user_input}"
    response = run_llama_cli(cpp_binary_path, agent, prompt, gpu_memory_percentage)
    chat_history.append((user_input, response.strip()))
    return chat_history