# .\main_script.py

import os
import time
from scripts.utility_misc import handle_config, monitor_resources, check_model_paths
from scripts.gradio_interface import launch_gradio_interface
import data.configure_temporary as config_temp

def main():
    config_path = './data/configure_persistent.json'
    if not os.path.exists(config_path):
        print("Configuration file not found.")
        return

    config = handle_config("load", config_path)
    config_temp.chat_model = config.get("chat_model_used")
    config_temp.instruct_model = config.get("instruct_model_used")
    config_temp.code_model = config.get("code_model_used")
    config_temp.max_memory_usage = config.get("maximum_memory_usage")

    if not check_model_paths([config_temp.chat_model, config_temp.instruct_model, config_temp.code_model]):
        print("Check model locations!")
        return

    # Launch the interface without loading the models
    launch_gradio_interface()

if __name__ == "__main__":
    main()
