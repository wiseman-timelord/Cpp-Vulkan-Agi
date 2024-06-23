# .\main_launch.py

import json
import subprocess
import os

def run_llama_cli(cpp_binary_path, model_path, gpu_memory_percentage):
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
        "-r", "User:"
    ]
    if gpu_memory_percentage:
        command += ["--gpu-memory", str(gpu_memory_percentage)]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running llama CLI: {e}")
        return None

def main():
    config_path = './data/config_general.json'
    if not os.path.exists(config_path):
        print("Configuration file not found. Please run main_config.py first.")
        return

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    current_model = config.get("current_model")
    cpp_binary_path = config.get("cpp_binary_path")
    gpu_memory_percentage = config.get("gpu_memory_percentage")

    if not current_model or not cpp_binary_path:
        print("Configuration not set properly. Please run main_config.py first.")
        return

    prompt = "Initial prompt to set up the model"
    response = run_llama_cli(cpp_binary_path, current_model, gpu_memory_percentage)
    if response:
        print(response)
    else:
        print("Failed to get response from the model.")

    # Proceed with setting up Gradio and other components

if __name__ == "__main__":
    main()
