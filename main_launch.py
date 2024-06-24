import os
from scripts.utility_general import load_config
from scripts.model_interaction import run_llama_cli

def main():
    config_path = './data/config_general.json'
    if not os.path.exists(config_path):
        print("Configuration file not found. Please run main_config.py first.")
        return

    config = load_config(config_path)
    current_model = config.get("current_model")
    processing_method_used = config.get("processing_method_used")
    max_memory_usage = config.get("maximum_memory_usage")

    if not current_model or not processing_method_used:
        print("Configuration not set properly. Please run main_config.py first.")
        return

    # Determine the cpp_binary_path based on the processing method
    cpp_binary_path = f'./libraries/llama-bin-win-{processing_method_used.lower()}-x64/llama-cli.exe'

    response = run_llama_cli(cpp_binary_path, current_model, max_memory_usage=max_memory_usage, use_gpu='vulkan' in processing_method_used.lower())
    if response:
        print(response)
    else:
        print("Failed to get response from the model.")

if __name__ == "__main__":
    main()
