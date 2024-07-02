# .\scripts\model_interact.py

import subprocess
from scripts.utilities_misc import monitor_resources, manage_models_in_gpu, manage_models_in_ram
import data.configure_temporary as config_temp

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
            print("Memory exceeded, unloading model!")
            manage_models_in_gpu(unload=True)
            return f"Memory exceeded, model unloaded! (Usage: {usage}%)"
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Error running llama CLI: {e}")
            return None

def generate_response(cpp_binary_path, model_path, user_input, chat_history, max_memory_usage, use_gpu=True):
    success, usage = monitor_resources(max_memory_usage, use_gpu)
    if not success:
        logger.error(f"Memory usage exceeded: {usage}%, unloading models!")
        manage_models_in_ram(unload=True)
        manage_models_in_gpu(unload=True)
        return f"Memory usage exceeded: {usage}%, unloading models!"

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
    if user_input:
        command.append("-p")
        command.append(user_input)

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running llama CLI: {e}")
        return None
