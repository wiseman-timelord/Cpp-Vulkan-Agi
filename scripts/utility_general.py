# .\scripts\utility_general.py - for, system, maintenance and calculation, code.

import os
import psutil
import json
import mmap

config_path = './data/config_general.json'

def load_config(config_path):
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    else:
        return {}

def save_config(config, config_path):
    with open(config_path, 'w') as config_file:
        json.dump(config, config_file)
    return "Configuration saved!"

def check_model_paths(model_paths):
    for path in model_paths:
        if not os.path.exists(path):
            return False
    return True

def load_model_to_ram(model_path):
    try:
        with open(model_path, "r+b") as f:
            mmapped_file = mmap.mmap(f.fileno(), 0)
            print(f"Loaded {model_path} to RAM.")
            return mmapped_file
    except Exception as e:
        print(f"Failed to load {model_path} to RAM: {e}")
        return None

def unload_models_from_ram(models):
    for model in models:
        try:
            model.close()
            print(f"Unloaded model from RAM.")
        except Exception as e:
            print(f"Failed to unload model from RAM: {e}")

def load_model_to_gpu(model_path):
    try:
        # Placeholder for actual logic to load a model to GPU using llama.cpp and Vulkan
        print(f"Loading {model_path} to GPU...")
        # Implement actual logic to load model to GPU here
        return True
    except Exception as e:
        print(f"Failed to load {model_path} to GPU: {e}")
        return False

def save_config_wrapper(current_model, processing_method, max_memory_usage):
    config = {
        "chat_model_used": current_model.get("chat_model_used", ""),
        "instruct_model_used": current_model.get("instruct_model_used", ""),
        "code_model_used": current_model.get("code_model_used", ""),
        "maximum_memory_usage": max_memory_usage
    }
    return save_config(config, config_path)

def load_config_wrapper():
    config = load_config(config_path)
    return {
        "chat_model_used": config.get("chat_model_used", ""),
        "instruct_model_used": config.get("instruct_model_used", ""),
        "code_model_used": config.get("code_model_used", ""),
        "maximum_memory_usage": config.get("maximum_memory_usage", 90)
    }

def load_models(chat_model, instruct_model, code_model):
    chat_model_ram = load_model_to_ram(chat_model)
    instruct_model_ram = load_model_to_ram(instruct_model)
    code_model_ram = load_model_to_ram(code_model)
    return [chat_model_ram, instruct_model_ram, code_model_ram]

def unload_models(models):
    unload_models_from_ram(models)
    print("All Models Unloaded.")

def monitor_resources(max_memory_usage, use_gpu=True):
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    if memory_percent > max_memory_usage:
        return False, memory_percent
    return True, memory_percent
