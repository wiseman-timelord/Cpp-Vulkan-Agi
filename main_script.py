# .\main_script.py - the main script.

import os
import time
import gradio as gr
from scripts.utility_script import load_config, check_model_paths, manage_models_in_ram, manage_models_in_gpu, monitor_resources
from scripts.model_interaction import run_llama_cli
from scripts.gradio_interface import launch_gradio_interface

def main():
    config_path = './data/config_general.json'
    if not os.path.exists(config_path):
        print("Configuration file not found. Please run main_config.py first.")
        return

    config = load_config(config_path)
    chat_model = config.get("chat_model_used")
    instruct_model = config.get("instruct_model_used")
    code_model = config.get("code_model_used")
    max_memory_usage = config.get("maximum_memory_usage")

    if not check_model_paths([chat_model, instruct_model, code_model]):
        print("Check Modelfile Locations Are Correct!")
        return

    models = manage_models_in_ram([chat_model, instruct_model, code_model])
    print("Models Loaded To System RAM.")

    if not manage_models_in_gpu(chat_model, max_memory_usage=max_memory_usage):
        print("Failed to load chat model to GPU.")
        return

    print("Chat Model Loaded On GPU.")

    launch_gradio_interface()

    while True:
        success, usage = monitor_resources(max_memory_usage, use_gpu=True)
        if not success:
            print(f"The maximum memory allowance was exceeded, unloading models! (Usage: {usage}%)")
            manage_models_in_ram(models, unload=True)
            manage_models_in_gpu(unload=True)
            break

        response = run_llama_cli(
            "./libraries/llama-bin-win-vulkan-x64/llama-cli.exe", chat_model, max_memory_usage=max_memory_usage, use_gpu=True
        )
        if response:
            print(response)
        else:
            print("Failed to get response from the model.")

        time.sleep(1)  # Monitor every second

if __name__ == "__main__":
    main()
