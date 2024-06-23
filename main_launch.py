# .\main_launch.py

import json
import subprocess

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

    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout


def main():
    with open('./data/config_general.json', 'r') as config_file:
        config = json.load(config_file)

    current_model = config["current_model"]
    cpp_binary_path = config["cpp_binary_path"]
    gpu_memory_percentage = config["gpu_memory_percentage"]

    if not current_model:
        print("Configuration not set. Please run main_config.py first.")
        return

    prompt = "Initial prompt to set up the model"
    response = run_llama_cli(cpp_binary_path, current_model, gpu_memory_percentage)
    print(response)  # Placeholder to show the initial model response

    # Proceed with setting up Gradio and other components

if __name__ == "__main__":
    main()
