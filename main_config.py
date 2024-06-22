# .\main_config.py

import json
import requests

def get_model_list():
    response = requests.get("http://localhost:8000/api/tags")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve models from Ollama.")
        return []

def select_model(models, selection):
    if selection.isdigit() and 1 <= int(selection) <= len(models):
        return models[int(selection) - 1]
    return None

def display_main_menu(current_model, current_processor, gpu_memory_percentage):
    print("\nMain Menu\n")
    print(f"1. Model Options\n(CurrentModel: {current_model[:20]})")
    print(f"2. Processor Options\n(CurrentProcessor: {current_processor})")
    print(f"3. GPU Memory Usage\n(CurrentUsage: {gpu_memory_percentage}%)")
    print("\n----------------------")
    print("Selection; Choose Options = 1-3, Exit Program = X:")

def display_model_menu(models):
    print("\nModel Selection:\n")
    for idx, model in enumerate(models, 1):
        print(f"{idx}. {model[:20]}...")
    print("\n----------------------")
    print("Selection; Choose Options = 1-{0}, Request Models = R, Exit Program = X:".format(len(models)))

def display_processor_menu(processors):
    print("\nProcessor Selection:\n")
    for idx, processor in enumerate(processors, 1):
        print(f"{idx}. {processor}")
    print("\n----------------------")
    print("Selection; Choose Options = 1-{0}, Exit Program = X:".format(len(processors)))

def get_user_selection():
    return input().strip().lower()

def main_config():
    processors = ["CPU AMD (AVX2)", "GPU AMD (OpenCL)", "GPU AMD (DirectML)"]
    current_model = "None"
    current_processor = "None"
    gpu_memory_percentage = 50

    config = {
        "current_model": current_model,
        "current_processor": current_processor,
        "gpu_memory_percentage": gpu_memory_percentage
    }

    while True:
        display_main_menu(current_model, current_processor, gpu_memory_percentage)
        main_selection = get_user_selection()

        if main_selection == '1':
            models = get_model_list()
            while not current_model:
                display_model_menu(models)
                model_selection = get_user_selection()

                if model_selection == 'r':
                    models = get_model_list()
                elif model_selection == 'x':
                    break
                else:
                    current_model = select_model(models, model_selection)
                    if not current_model:
                        print("Invalid selection. Please try again.")
                    else:
                        config["current_model"] = current_model

        elif main_selection == '2':
            while not current_processor:
                display_processor_menu(processors)
                processor_selection = get_user_selection()

                if processor_selection == 'x':
                    break
                else:
                    if processor_selection.isdigit() and 1 <= int(processor_selection) <= len(processors):
                        current_processor = processors[int(processor_selection) - 1]
                        config["current_processor"] = current_processor
                    else:
                        print("Invalid selection. Please try again.")
        
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
