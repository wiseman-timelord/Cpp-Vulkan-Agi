# .\scripts\model_interaction.py - for interaction with the models.

import subprocess
from scripts.utility_script import monitor_resources, manage_models_in_gpu

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
