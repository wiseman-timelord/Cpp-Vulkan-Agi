# .\main_config.py

import json
import requests

def get_model_list():
    OLLAMA_API_URL = "http://localhost:8000/api/tags"  # Ensure this is the correct API endpoint
    response = requests.get(OLLAMA_API_URL)
    if response.status_code == 200:
        return response.json()  # Assuming the response is a JSON list of models
    else:
        print("Failed to retrieve models from Ollama.")
        return []

def select_model(models, selection):
    if selection.isdigit() and 1 <= int(selection) <= len(models):
        return models[int(selection) - 1]
    return None

def display_main_menu(current_model, current_processor):
    print("\nMain Menu\n")
    print(f"1. Model Options\n(CurrentModel: {current_model[:20]})")
    print(f"2. Processor Options\n(CurrentProcessor: {current_processor})")
    print("\n----------------------")
    print("Selection; Choose Options = 1-2, Exit Program = X:")

def display_model_menu(models):
    print("\nModel Selection:\n")
    for idx, model in enumerate(models, 1):
        print(f"{idx}. {model[:20]}...")
    print("\n----------------------")
    print("Selection; Choose Options = 1-{0}, Request Models = R, Exit Program = X:".format(len(models)))

def display_processor_menu(processors):
    print("\nModel Processing:\n")
    for idx, processor in enumerate(processors, 1):
        print(f"{idx}. {processor}")
    print("\n----------------------")
    print("Selection; Choose Options = 1-{0}, Exit Program = X:".format(len(processors)))

def get_user_selection():
    return input().strip().lower()

def main_config():
    processors = ["CPU AMD", "CPU Intel", "GPU AMD", "GPU NVIDIA"]
    current_model = "None"
    current_processor = "None"
    selected_model = None
    selected_processor = None

    config = {
        "current_model": current_model,
        "current_processor": current_processor
    }

    while True:
        display_main_menu(current_model, current_processor)
        main_selection = get_user_selection()

        if main_selection == '1':
            models = get_model_list()
            while not selected_model:
                display_model_menu(models)
                model_selection = get_user_selection()

                if model_selection == 'r':
                    models = get_model_list()
                elif model_selection == 'x':
                    selected_model = None
                    break
                else:
                    selected_model = select_model(models, model_selection)
                    if not selected_model:
                        print("Invalid selection. Please try again.")
                    else:
                        current_model = selected_model
                        config["current_model"] = current_model

        elif main_selection == '2':
            while not selected_processor:
                display_processor_menu(processors)
                processor_selection = get_user_selection()

                if processor_selection == 'x':
                    selected_processor = None
                    break
                else:
                    if processor_selection.isdigit() and 1 <= int(processor_selection) <= len(processors):
                        selected_processor = processors[int(processor_selection) - 1]
                        current_processor = selected_processor
                        config["current_processor"] = current_processor
                    else:
                        print("Invalid selection. Please try again.")

        elif main_selection == 'x':
            print("Exiting configuration setup.")
            break

    # Save configuration to JSON
    with open('./data/config_general.json', 'w') as config_file:
        json.dump(config, config_file)

if __name__ == "__main__":
    main_config()
