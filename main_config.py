# .\main_config.py

import json
import os

def display_main_menu(current_model, graphics_method, gpu_memory_percentage):
    os.system('cls')
    print("\n=================( Main Configurator Menu )==============\n\n")
    print(f"1. Model Location\n(CurrentModel: {shorten_path(current_model, 35)})\n")
    print(f"2. Graphics Method\n(CurrentMethod: {graphics_method})\n")
    print(f"3. GPU Memory Usage\n(CurrentUsage: {gpu_memory_percentage}%)\n")
    print("\n---------------------------------------------------------")
    print("Selection; Choose Options = 1-3, Exit & Save = X:")

def shorten_path(path, length):
    if len(path) > length:
        return "..." + path[-(length-3):]
    return path

def get_user_selection():
    return input().strip().lower()

def load_config():
    default_config = {
        "current_model": ".\\ModelFolder\\ModelFile.GGUF",
        "graphics_method": "OpenCL",
        "gpu_memory_percentage": 50
    }
    
    try:
        with open('./data/config_general.json', 'r') as config_file:
            config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        config = default_config
    
    # Ensure all necessary keys are present, use default values if not
    for key in default_config:
        if key not in config or not config[key]:
            config[key] = default_config[key]
    
    return config

def main_config():
    config = load_config()
    
    current_model = config["current_model"]
    graphics_method = config["graphics_method"]
    gpu_memory_percentage = config["gpu_memory_percentage"]

    while True:
        display_main_menu(current_model, graphics_method, gpu_memory_percentage)
        main_selection = get_user_selection()

        if main_selection == '1':
            current_model = input("Enter the full path to the model file: ").strip()
            config["current_model"] = current_model

        elif main_selection == '2':
            graphics_method = "DirectML" if graphics_method == "OpenCL" else "OpenCL"
            config["graphics_method"] = graphics_method

        elif main_selection == '3':
            new_gpu_memory_percentage = input("Enter new GPU memory usage percentage (10-100): ").strip()
            if new_gpu_memory_percentage.isdigit() and 10 <= int(new_gpu_memory_percentage) <= 100:
                gpu_memory_percentage = int(new_gpu_memory_percentage)
                config["gpu_memory_percentage"] = gpu_memory_percentage
            else:
                print("Invalid percentage. Please try again.")

        elif main_selection == 'x':
            print("Exiting configuration setup.")
            break

    with open('./data/config_general.json', 'w') as config_file:
        json.dump(config, config_file)

if __name__ == "__main__":
    main_config()
