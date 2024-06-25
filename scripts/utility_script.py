# .\scripts\utility_script.py

import os, mmap, json, psutil, ctypes, gc, subprocess
import vulkan as vk
from llama_cpp import Llama

config_path = './data/config_general.json'

class VulkanModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.instance = self.get_vulkan_instance()
        self.physical_device = self.get_physical_device()
        self.device = None
        self.model = None
    
    def get_vulkan_instance(self):
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
    
    def get_physical_device(self):
        physical_devices = vk.vkEnumeratePhysicalDevices(self.instance)
        return physical_devices[0]  # Assuming there's at least one device

    def load_model_to_gpu(self):
        try:
            self.model = Llama(model_path=self.model_path, n_gpu_layers=40)
            print(f"Model {self.model_path} loaded to GPU")
            return True
        except Exception as e:
            print(f"Failed to load model to GPU: {e}")
            return False

    def unload_model_from_gpu(self):
        try:
            if self.model:
                del self.model
                self.model = None
                gc.collect()
                print(f"Model {self.model_path} unloaded from GPU")
            
            if self.device:
                vk.vkDestroyDevice(self.device, None)
                self.device = None

            if self.instance:
                vk.vkDestroyInstance(self.instance, None)
                self.instance = None

            print("Vulkan resources cleaned up")
        except Exception as e:
            print(f"Failed to unload model and clean up Vulkan resources: {e}")

def unload_models_from_gpu():
    try:
        if vulkan_model_instance:
            vulkan_model_instance.unload_model_from_gpu()
    except Exception as e:
        print(f"Failed to unload models from GPU: {e}")

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
    return physical_devices[0]  # Assuming there's at least one device

def get_vram_usage(instance, physical_device):
    memory_properties = vk.vkGetPhysicalDeviceMemoryProperties(physical_device)
    memory_heaps = memory_properties.memoryHeaps

    total_vram = sum(heap.size for heap in memory_heaps if heap.flags & vk.VK_MEMORY_HEAP_DEVICE_LOCAL_BIT)
    device_memory_properties = vk.vkGetPhysicalDeviceMemoryProperties(physical_device)
    device_memory_heap = device_memory_properties.memoryHeaps[0]
    committed_memory = vk.vkGetDeviceMemoryCommitment(physical_device)
    used_vram = committed_memory / total_vram * 100  # Convert to percentage

    return used_vram

def monitor_vram_usage(instance, physical_device, max_memory_usage):
    used_vram = get_vram_usage(instance, physical_device)
    if used_vram > max_memory_usage:
        return False, used_vram
    return True, used_vram

def load_model_to_gpu(model_path, max_memory_usage):
    try:
        instance = get_vulkan_instance()
        physical_device = get_physical_device(instance)
        
        success, used_vram = monitor_vram_usage(instance, physical_device, max_memory_usage)
        if not success:
            print("GPU VRam Exceeded, Unloading Models...")
            unload_models_from_gpu()
            return False
        
        command = [
            "./libraries/llama-bin-win-vulkan-x64/llama-cli.exe",
            "-m", model_path,
            "--n-gpu-layers", "1000000",  # Example to load fully into GPU
            "--main-gpu", "0"
        ]
        
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            print(f"Failed to load {model_path} to GPU: {stderr.decode('utf-8')}")
            return False
        
        print(f"Loading {model_path} to GPU: {stdout.decode('utf-8')}")
        return True
    except Exception as e:
        print(f"Failed to load {model_path} to GPU: {e}")
        return False
