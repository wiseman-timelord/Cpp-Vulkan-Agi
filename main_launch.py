# .\main_interface.py

import json
from scripts.menu_display import launch_gradio_interface
from scripts.model_interaction import initialize_model, setup_agents

def main():
    # Load configuration from JSON
    with open('./data/config_general.json', 'r') as config_file:
        config = json.load(config_file)

    current_model = config["current_model"]
    current_processor = config["current_processor"]

    if current_model == "None" or current_processor == "None":
        print("Configuration not set. Please run main_config.py first.")
        return

    if "GPU AMD" in current_processor:
        device = "directml"
    else:
        device = "cpu"

    model, tokenizer, device = initialize_model(current_model, device)
    agents = setup_agents(current_model, device)
    launch_gradio_interface(agents, tokenizer, device)


if __name__ == "__main__":
    main()
