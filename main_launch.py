# .\main_launch.py

import json, subprocess, psutil. os

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

def run_llama_cli(cpp_binary_path, model_path, max_memory_usage, use_gpu=True):
    command = [
        cpp_binary_path,
        "-m", model_path,
        "-c", "512",
        "-b", "1024",
        "-n", "256",
        "--keep", "48",
        "--repeat_penalty", "1.0",
        "--color",
        "-i",
        "-r", "User:"
    ]

    while True:
        success, usage = monitor_resources(max_memory_usage, use_gpu)
        if not success:
            print(f"The maximum memory allowance was exceeded, model un-loaded!")
            return f"The maximum memory allowance was exceeded, model un-loaded! (Usage: {usage}%)"
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error running llama CLI: {e}")
            return None

def main():
    config_path = './data/config_general.json'
    if not os.path.exists(config_path):
        print("Configuration file not found. Please run main_config.py first.")
        return

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    current_model = config.get("current_model")
    cpp_binary_path = config.get("cpp_binary_path")
    max_memory_usage = config.get("maximum_memory_usage")

    if not current_model or not cpp_binary_path:
        print("Configuration not set properly. Please run main_config.py first.")
        return

    response = run_llama_cli(cpp_binary_path, current_model, max_memory_usage, use_gpu='vulkan' in cpp_binary_path)
    if response:
        print(response)
    else:
        print("Failed to get response from the model.")

if __name__ == "__main__":
    main()