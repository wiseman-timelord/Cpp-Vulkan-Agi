import time, os, subprocess, requests, shutil, zipfile
from tqdm import tqdm

LLAMA_VERSION = "b3206"
SUFFIXES = ["vulkan-x64"]

def print_install_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n===================( Installing Your Selection )=================\n")

def display_main_menu():
    window_width = 65
    window_height = 25
    
    def pad_center(text, width):
        return text.center(width)

    while True:
        os.system('mode con: cols={} lines={}'.format(window_width, window_height))
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n========================( Setup-Installer )=======================\n\n\n\n\n\n\n")
        print(pad_center("1. Install Requirements", window_width))
        print(pad_center("(pip install -r requirements.txt)\n", window_width))
        print(pad_center("2. Install GitHub Libraries", window_width))
        print(pad_center(f"(Llama.Cpp: {LLAMA_VERSION})", window_width))
        print("\n\n\n\n\n\n" + "-" * window_width)
        print("Selection; Choose Options = 1-2, Exit Config = X:", end=' ')

        main_selection = get_user_selection()

        if main_selection == '1':
            install_requirements()
            time.sleep(2)

        elif main_selection == '2':
            install_github_libraries()
            time.sleep(2)

        elif main_selection == 'x':
            print("Exiting configuration setup.")
            time.sleep(2)
            break

def get_user_selection():
    return input().strip().lower()

def install_requirements():
    print_install_title()
    print("\nInstalling requirements...\n")
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
        print("\nRequirements installed successfully.")
    else:
        print("\nFailed to install some requirements.")
    time.sleep(5)

def download_and_extract(url, extract_to):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join('.\\cache', local_filename)
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    with open(local_filepath, 'wb') as f, tqdm(
            desc=local_filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            bar_format="{desc}: {percentage:3.0f}%|{bar:20}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
    ) as bar:
        for data in response.iter_content(block_size):
            f.write(data)
            bar.update(len(data))
    
    with zipfile.ZipFile(local_filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def install_github_libraries():
    print_install_title()
    print("\nInstalling GitHub libraries...\n")
    
    llama_urls = [f"https://github.com/ggerganov/llama.cpp/releases/download/{LLAMA_VERSION}/llama-{LLAMA_VERSION}-bin-win-{suffix}.zip" for suffix in SUFFIXES]
    llama_destinations = [f".\\libraries\\llama-bin-win-{suffix}\\" for suffix in SUFFIXES]

    # Install Llama binaries
    for suffix, url, dest in zip(SUFFIXES, llama_urls, llama_destinations):
        binary_path = os.path.join(dest, "llama-cli.exe")
        if os.path.exists(binary_path):
            print(f"Binary already exists at {binary_path}, skipping download.")
            continue
        print(f"Downloading and extracting {url} to {dest}...")
        os.makedirs(dest, exist_ok=True)
        try:
            download_and_extract(url, dest)
            # Ensure the extracted folder is renamed correctly
            extracted_dir = f".\\libraries\\llama-{LLAMA_VERSION}-bin-win-{suffix}\\"
            if os.path.exists(extracted_dir):
                shutil.move(extracted_dir, dest)
        except Exception as e:
            print(f"Failed to download or extract {url}. Reason: {e}")

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

    print("\nGitHub libraries installed successfully.")
    time.sleep(5)


if __name__ == "__main__":
    display_main_menu()
