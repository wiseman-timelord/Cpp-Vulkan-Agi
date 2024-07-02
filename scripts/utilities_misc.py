# .\scripts\utilities_misc.py

import os, mmap, json, psutil, ctypes, gc, subprocess, time, random
import vulkan as vk
from llama_cpp import Llama
import logging  # Ensure logging is imported

logger = logging.getLogger(__name__)

def get_vulkan_instance():
    try:
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

        return vk.vkCreateInstance(create_info, None)
    except Exception as e:
        logger.error(f"Failed to create Vulkan instance: {e}")
        raise

def get_logical_device(instance, physical_device):
    queue_family_index = 0  # Example index, determine queue family index
    device_queue_create_info = vk.VkDeviceQueueCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO,
        queueFamilyIndex=queue_family_index,
        queueCount=1,
        pQueuePriorities=[1.0]
    )

    device_create_info = vk.VkDeviceCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO,
        queueCreateInfoCount=1,
        pQueueCreateInfos=[device_queue_create_info],
    )

    return vk.vkCreateDevice(physical_device, device_create_info, None)

def get_physical_device(instance):
    return vk.vkEnumeratePhysicalDevices(instance)[0]

def get_vram_usage(instance, physical_device, device):
    memory_properties = vk.vkGetPhysicalDeviceMemoryProperties(physical_device)
    memory_heaps = memory_properties.memoryHeaps
    total_vram = sum(heap.size for heap in memory_heaps if heap.flags & vk.VK_MEMORY_HEAP_DEVICE_LOCAL_BIT)
    memory_type_index = next(
        (i for i, mt in enumerate(memory_properties.memoryTypes) if mt.propertyFlags & vk.VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT), None)
    if memory_type_index is None:
        raise RuntimeError("No suitable memory type.")

    allocate_info = vk.VkMemoryAllocateInfo(
        sType=vk.VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO,
        allocationSize=1024 * 1024,  # Example allocation size, adjust as needed
        memoryTypeIndex=memory_type_index,
    )
    device_memory = vk.vkAllocateMemory(device, allocate_info, None)
    committed_memory = vk.vkGetDeviceMemoryCommitment(device, device_memory)
    vk.vkFreeMemory(device, device_memory, None)
    return (committed_memory / total_vram) * 100

def monitor_vram_usage(instance, physical_device, device, max_memory_usage):
    used_vram = get_vram_usage(instance, physical_device, device)
    return (used_vram <= max_memory_usage), used_vram

def monitor_resources(max_memory_usage, use_gpu=True):
    if use_gpu:
        instance = get_vulkan_instance()
        physical_device = get_physical_device(instance)
        device = get_logical_device(instance, physical_device)
        return monitor_vram_usage(instance, physical_device, device, max_memory_usage)
    else:
        mem = psutil.virtual_memory()
        return (mem.percent <= max_memory_usage), mem.percent

def manage_models_in_gpu(model_path=None, unload=False, max_memory_usage=None):
    if unload:
        try:
            if model_path:
                del model_path
                gc.collect()
            print("Model unloaded from GPU")
        except Exception as e:
            logger.error(f"GPU unload failed: {e}")
        return

    try:
        instance = get_vulkan_instance()
        physical_device = get_physical_device(instance)
        device = get_logical_device(instance, physical_device)
        
        success, used_vram = monitor_vram_usage(instance, physical_device, device, max_memory_usage)
        if not success:
            print("VRAM exceeded, unloading models...")
            manage_models_in_gpu(unload=True)
            return False
        
        model = Llama(model_path=model_path, n_gpu_layers=40)
        print("Model loaded to GPU")
        return True
    except Exception as e:
        logger.error(f"GPU load failed: {e}")
        return False

def handle_config(action, config_path, config=None):
    if action == "load":
        if os.path.exists(config_path):
            with open(config_path, 'r') as config_file:
                return json.load(config_file)
        else:
            return {}
    elif action == "save" and config is not None:
        with open(config_path, 'w') as config_file:
            json.dump(config, config_file)
        return "Configuration saved!"

def check_model_paths(model_paths, config_path):
    config_updated = False
    config = handle_config("load", config_path)

    for idx, path in enumerate(model_paths):
        if not os.path.exists(path):
            if idx == 0:
                config_temp.chat_model = ""
                config["chat_model_used"] = ""
            elif idx == 1:
                config_temp.instruct_model = ""
                config["instruct_model_used"] = ""
            elif idx == 2:
                config_temp.code_model = ""
                config["code_model_used"] = ""
            config_updated = True

    if config_updated:
        handle_config("save", config_path, config)

def manage_models_in_ram(model_paths, unload=False):
    models = []
    if unload:
        for model in model_paths:
            try:
                model.close()
                print("Model unloaded from RAM.")
            except Exception as e:
                print(f"RAM unload failed: {e}")
        return

    for model_path in model_paths:
        try:
            with open(model_path, "r+b") as f:
                mmapped_file = mmap.mmap(f.fileno(), 0)
                models.append(mmapped_file)
                print(f"Loaded {model_path} to RAM.")
        except Exception as e:
            print(f"RAM load failed: {e}")

    return models
