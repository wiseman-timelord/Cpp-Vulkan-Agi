import json
import psutil
import os
import pynvml

config_path = './data/config_general.json'

def get_gpu_memory_usage():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # Assuming a single GPU setup; modify for multiple GPUs
    mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    gpu_memory_usage_percent = (mem_info.used / mem_info.total) * 100
    pynvml.nvmlShutdown()
    return gpu_memory_usage_percent

def monitor_resources(max_memory_usage, use_gpu=True):
    if use_gpu:
        gpu_memory_usage = get_gpu_memory_usage()
        if gpu_memory_usage > max_memory_usage:
            return False, gpu_memory_usage
    else:
        cpu_memory = psutil.virtual_memory()
        cpu_memory_usage = cpu_memory.percent
        if cpu_memory_usage > max_memory_usage:
            return False, cpu_memory_usage
    return True, None

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

def save_config_wrapper(current_model, processing_method, max_memory_usage):
    config = {
        "current_model": current_model,
        "processing_method_used": processing_method,
        "maximum_memory_usage": max_memory_usage
    }
    return save_config(config, config_path)

def load_config_wrapper():
    config = load_config(config_path)
    return config.get("current_model", ""), config.get("processing_method_used", "AVX2"), config.get("maximum_memory_usage", 90)
