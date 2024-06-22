import json
import os
import subprocess
from datetime import datetime
import requests
import zipfile
import shutil

def display_main_menu(current_model, cpp_binary_used, gpu_memory_percentage, requirement_update):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=================( Main Configurator Menu )==============\n\n")
    print(f"1. Install Requirements\n(Last Updated: {requirement_update})\n")
    print(f"2. Install Llama Binaries\n(BinariesVersion: b3197)\n")
    print(f"3. Model Location\n(CurrentModel: {shorten_path(current_model, 35)})\n")
    print(f"4. Processing Method\n(CurrentMethod: {cpp_binary_used})\n")
    print(f"5. GPU Memory Usage\n(CurrentUsage: {gpu_memory_percentage}%)\n")
    print("\n---------------------------------------------------------")
    print("Selection; Choose Options = 1-5, Exit & Save = X:")

def shorten_path(path, length):
    if len(path) > length:
        return "..." + path[-(length-3):]
    return path

def get_user_selection():
    return input().strip().lower()

def load_config():
    default_config = {
        "current_model": ".\\ModelFolder\\ModelFile.GGUF",
        "cpp_binary_used": "OpenBLAS",
        "gpu_memory_percentage": 50,
        "requirement_update": "Never"
    }
    
    try:
        with open('.\\data\\config_general.json', 'r') as config_file:
            config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        config = default_config
    
    # Ensure all necessary keys are present, use default values if not
    for key in default_config:
        if key not in config or not config[key]:
            config[key] = default_config[key]
    
    return config

def install_requirements():
    print("Installing requirements...")
    command = [
        "pip", "install", 
        "--requirement", ".\\requirements.txt",
        "--retries", "5",
        "--timeout", "15",
        "--no-cache-dir",
        "--progress-bar", "on"
    ]
    result = subprocess.run(command)
    if result.returncode == 0:
        print("Requirements installed successfully.")
        return datetime.now().strftime("%Y/%m/%d")
    else:
        print("Failed to install some requirements.")
        return None
    input("Press Enter to return to the main menu...")

def download_and_extract(url, extract_to):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join('.\\cache', local_filename)
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    with zipfile.ZipFile(local_filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def install_llama_binaries():
    urls = [
        "https://github.com/ggerganov/llama.cpp/releases/download/b3197/llama-b3197-bin-win-vulkan-x64.zip",
        "https://github.com/ggerganov/llama.cpp/releases/download/b3197/llama-b3197-bin-win-openblas-x64.zip",
        "https://github.com/ggerganov/llama.cpp/releases/download/b3197/llama-b3197-bin-win-avx2-x64.zip",
        "https://github.com/ggerganov/llama.cpp/releases/download/b3197/llama-b3197-bin-win-avx-x64.zip",
        "https://github.com/ggerganov/llama.cpp/releases/download/b3197/llama-b3197-bin-win-avx512-x64.zip"
    ]
    destinations = [
        ".\\data\\llama-b3197-bin-win-vulkan-x64\\",
        ".\\data\\llama-b3197-bin-win-openblas-x64\\",
        ".\\data\\llama-b3197-bin-win-avx2-x64\\",
        ".\\data\\llama-b3197-bin-win-avx-x64\\",
        ".\\data\\llama-b3197-bin-win-avx512-x64\\"
    ]

    for url, dest in zip(urls, destinations):
        print(f"Downloading and extracting {url} to {dest}...")
        os.makedirs(dest, exist_ok=True)
        download_and_extract(url, dest)
    
    # Clean up cache directory
    for filename in os.listdir('.\\cache'):
        if filename != "placeholder":
            file_path = os.path.join('.\\cache', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    input("Llama binaries installed successfully. Press Enter to return to the main menu...")

def main_config():
    config = load_config()
    
    current_model = config["current_model"]
    cpp_binary_used = config["cpp_binary_used"]
    gpu_memory_percentage = config["gpu_memory_percentage"]
    requirement_update = config["requirement_update"]

    while True:
        display_main_menu(current_model, cpp_binary_used, gpu_memory_percentage, requirement_update)
        main_selection = get_user_selection()

        if main_selection == '1':
            new_update_date = install_requirements()
            if new_update_date:
                requirement_update = new_update_date
                config["requirement_update"] = requirement_update

        elif main_selection == '2':
            install_llama_binaries()

        elif main_selection == '3':
            current_model = input("Enter the full path to the model file: ").strip()
            config["current_model"] = current_model

        elif main_selection == '4':
            cpp_binaries = ["AVX", "AVX2", "AVX512", "OpenBLAS", "Vulkan"]
            for i, binary in enumerate(cpp_binaries, start=1):
                print(f"{i}. {binary}")
            choice = int(input("Select the binary option (1-5): ").strip())
            if 1 <= choice <= 5:
                cpp_binary_used = cpp_binaries[choice - 1]
                config["cpp_binary_used"] = cpp_binary_used
            else:
                print("Invalid selection. Please try again.")

        elif main_selection == '5':
            new_gpu_memory_percentage = input("Enter new GPU memory usage percentage (10-100): ").strip()
            if new_gpu_memory_percentage.isdigit() and 10 <= int(new_gpu_memory_percentage) <= 100:
                gpu_memory_percentage = int(new_gpu_memory_percentage)
                config["gpu_memory_percentage"] = gpu_memory_percentage
            else:
                print("Invalid percentage. Please try again.")

        elif main_selection == 'x':
            print("Exiting configuration setup.")
            break

    with open('.\\data\\config_general.json', 'w') as config_file:
        json.dump(config, config_file)

if __name__ == "__main__":
    main_config()
