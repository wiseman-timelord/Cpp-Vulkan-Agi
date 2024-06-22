# .\main_launch.py

import json
import ollama

def initialize_ollama_model(model_name):
    ollama.pull(model_name)

def main():
    with open('./data/config_general.json', 'r') as config_file:
        config = json.load(config_file)

    current_model = config["current_model"]
    current_processor = config["current_processor"]
    gpu_memory_percentage = config["gpu_memory_percentage"]

    if current_model == "None" or current_processor == "None":
        print("Configuration not set. Please run main_config.py first.")
        return

    if "GPU AMD" in current_processor:
        device = "gpu"
        gpu_memory_limit = f"{gpu_memory_percentage}%"
    else:
        device = "cpu"
        gpu_memory_limit = None

    initialize_ollama_model(current_model)

    model, tokenizer = initialize_model(current_model, device, gpu_memory_limit)
    agents = setup_agents(current_model, device)
    launch_gradio_interface(agents, tokenizer, device)

def initialize_model(model_name, device, gpu_memory_limit=None):
    if device == "gpu":
        import torch_directml
        dml = torch_directml.device()
        if gpu_memory_limit:
            torch_directml.set_memory_fraction(float(gpu_memory_limit.strip('%')) / 100.0, dml)
        model = ollama.chat(model=model_name, messages=[], device=dml)
        tokenizer = ollama.AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer
    else:
        model = ollama.chat(model=model_name, messages=[])
        tokenizer = ollama.AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer

if __name__ == "__main__":
    main()
