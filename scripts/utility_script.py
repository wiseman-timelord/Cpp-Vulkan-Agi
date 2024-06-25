# .\scripts\utility_script.py - Calculations, File Operations, Shared functions, etc.

import os
import mmap
import json
import psutil
import ctypes
import gc
import subprocess
import vulkan as vk
from llama_cpp import Llama

config_path = './data/config_general.json'

def get_vulkan_instance():
    app_info = vk.VkApplicationInfo(
        sType=vk.VK_STRUCTURE_TYPE_APPLICATION_INFO,
        pApplicationName="VRAM Monitor",
        applicationVersion=vk.VK_MAKE_VERSION(1, 0, 0),
        pEngineName="No Engine",
        engineVersion=vk.VK_MAKE_VERSION(1, 0, 0),
        apiVersion=vk.VK_API_VERSION_1_0,
    )

    create_info = vk.VkInstanceCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
        pApplicationInfo=app_info,
    )

    instance = vk.vkCreateInstance(create_info, None)
    return instance

def get_physical_device(instance):
    physical_devices = vk.vkEnumeratePhysicalDevices(instance)
    return physical_devices[0]

def get_vram_usage(instance, physical_device):
    memory_properties = vk.vkGetPhysicalDeviceMemoryProperties(physical_device)
    memory_heaps = memory_properties.memoryHeaps

    total_vram = sum(heap.size for heap in memory_heaps if heap.flags & vk.VK_MEMORY_HEAP_DEVICE_LOCAL_BIT)
    device_memory_properties = vk.vkGetPhysicalDeviceMemoryProperties(physical_device)
    device_memory_heap = device_memory_properties.memoryHeaps[0]
    committed_memory = vk.vkGetDeviceMemoryCommitment(physical_device)
    used_vram = committed_memory / total_vram * 100

    return used_vram

def monitor_vram_usage(instance, physical_device, max_memory_usage):
    used_vram = get_vram_usage(instance, physical_device)
    if used_vram > max_memory_usage:
        return False, used_vram
    return True, used_vram

def monitor_resources(max_memory_usage, use_gpu=True):
    if use_gpu:
        instance = get_vulkan_instance()
        physical_device = get_physical_device(instance)
        success, usage = monitor_vram_usage(instance, physical_device, max_memory_usage)
    else:
        mem = psutil.virtual_memory()
        usage = mem.percent
        success = usage <= max_memory_usage

    return success, usage

def manage_models_in_gpu(model_path=None, unload=False, max_memory_usage=None):
    if unload:
        try:
            if model_path:
                del model_path
                gc.collect()
            print(f"Model {model_path} unloaded from GPU")
        except Exception as e:
            print(f"Failed to unload model from GPU: {e}")
        return

    try:
        instance = get_vulkan_instance()
        physical_device = get_physical_device(instance)
        
        success, used_vram = monitor_vram_usage(instance, physical_device, max_memory_usage)
        if not success:
            print("GPU VRam Exceeded, Unloading Models...")
            manage_models_in_gpu(unload=True)
            return False
        
        model = Llama(model_path=model_path, n_gpu_layers=40)
        print(f"Model {model_path} loaded to GPU")
        return True
    except Exception as e:
        print(f"Failed to load model to GPU: {e}")
        return False

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

def manage_models_in_ram(model_paths, unload=False):
    models = []
    if unload:
        for model in model_paths:
            try:
                model.close()
                print(f"Unloaded model from RAM.")
            except Exception as e:
                print(f"Failed to unload model from RAM: {e}")
        return

    for model_path in model_paths:
        try:
            with open(model_path, "r+b") as f:
                mmapped_file = mmap.mmap(f.fileno(), 0)
                models.append(mmapped_file)
                print(f"Loaded {model_path} to RAM.")
        except Exception as e:
            print(f"Failed to load {model_path} to RAM: {e}")

    return models
