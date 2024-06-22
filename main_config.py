# .\config_general.py

import json, time, os, subprocess, requests, shutil, zipfile
from datetime import datetime
from tqdm import tqdm

def display_main_menu(current_model, cpp_binary_path, gpu_memory_percentage, requirement_update, config):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        current_method_display = os.path.basename(os.path.dirname(cpp_binary_path))
        print("\n=================( Main Configurator Menu )==============\n")
        print("\n                  1. Install Requirements")
        print(f"                        ({requirement_update})")
        print("\n                 2. Install Llama Binaries")
        print("                          (b3197)")
        print("\n                   3. Processing Method")
        print(f"             ({current_method_display})")
        print("\n                   4. GPU Memory Usage")
        print(f"                           ({gpu_memory_percentage}%)")
        print("\n                  5. GGUF Model Location")
        print(f"              ({shorten_path(current_model, 35)})")
        print("\n\n---------------------------------------------------------")
        print("Selection; Choose Options = 1-5, Exit & Save = X:", end=' ')

        main_selection = get_user_selection()

        if main_selection == '1':
            new_update_date = install_requirements()
            if new_update_date:
                requirement_update = new_update_date
                config["requirement_update"] = requirement_update
                time.sleep(2)

        elif main_selection == '2':
            install_llama_binaries()
            time.sleep(2)

        elif main_selection == '3':
            cpp_binary_path = toggle_processing_method(config["cpp_binary_path"])
            config["cpp_binary_path"] = cpp_binary_path

        elif main_selection == '4':
            new_gpu_memory_percentage = input("Enter new GPU memory usage percentage (10-100): ").strip()
            if new_gpu_memory_percentage.isdigit() and 10 <= int(new_gpu_memory_percentage) <= 100:
                gpu_memory_percentage = int(new_gpu_memory_percentage)
                config["gpu_memory_percentage"] = gpu_memory_percentage
                time.sleep(1)
            else:
                print("Invalid percentage. Please try again.")
                time.sleep(2)

        elif main_selection == '5':
            current_model = input("Enter the full path to the model file: ").strip()
            config["current_model"] = current_model
            time.sleep(2)

        elif main_selection == 'x':
            print("Exiting configuration setup.")
            time.sleep(2)
            break

    with open('.\\data\\config_general.json', 'w') as config_file:
        json.dump(config, config_file)

def toggle_processing_method(current_cpp_binary_path):
    cpp_binaries = [
        ".\\data\\llama-b3197-bin-win-avx-x64\\llama-cli.exe",
        ".\\data\\llama-b3197-bin-win-avx2-x64\\llama-cli.exe",
        ".\\data\\llama-b3197-bin-win-avx512-x64\\llama-cli.exe",
        ".\\data\\llama-b3197-bin-win-openblas-x64\\llama-cli.exe",
        ".\\data\\llama-b3197-bin-win-vulkan-x64\\llama-cli.exe"
    ]
    
    current_index = cpp_binaries.index(current_cpp_binary_path)
    new_index = (current_index + 1) % len(cpp_binaries)
    
    return cpp_binaries[new_index]

def shorten_path(path, length):
    if len(path) > length:
        return "..." + path[-(length-3):]
    return path

def get_user_selection():
    return input().strip().lower()

def load_config():
    default_config = {
        "current_model": ".\\ModelFolder\\ModelFile.GGUF",
        "cpp_binary_path": ".\\data\\llama-b3197-bin-win-openblas-x64\\llama-cli.exe",
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
        update_date = datetime.now().strftime("%Y/%m/%d")
        return update_date
    else:
        print("Failed to install some requirements.")
        input("Review the error, then press Enter...")
        return None

def download_and_extract(url, extract_to):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join('.\\cache', local_filename)
    
    # Download file with progress bar
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    with open(local_filepath, 'wb') as f, tqdm(
            desc=local_filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            f.write(data)
            bar.update(len(data))
    
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
        binary_path = os.path.join(dest, "llama-cli.exe")
        if os.path.exists(binary_path):
            print(f"Binary already exists at {binary_path}, skipping download.")
            continue
        print(f"Downloading and extracting {url} to {dest}...")
        os.makedirs(dest, exist_ok=True)
        try:
            download_and_extract(url, dest)
        except Exception as e:
            print(f"Failed to download or extract {url}. Reason: {e}")
            input("Review the error, then press Enter to continue...")
    
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

    print("Llama binaries installed successfully.")

def main_config():
    config = load_config()
    
    current_model = config["current_model"]
    cpp_binary_path = config["cpp_binary_path"]
    gpu_memory_percentage = config["gpu_memory_percentage"]
    requirement_update = config["requirement_update"]

    display_main_menu(current_model, cpp_binary_path, gpu_memory_percentage, requirement_update, config)

if __name__ == "__main__":
    main_config()
