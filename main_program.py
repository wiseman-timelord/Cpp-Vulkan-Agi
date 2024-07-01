# .\main_program.py

import os
import logging
from scripts.utility_misc import handle_config, check_model_paths
from scripts.gradio_interface import launch_gradio_interface
import data.configure_temporary as config_temp

# Initialize logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def main():
    config_path = './data/configure_persistent.json'
    if not os.path.exists(config_path):
        logger.error("Configuration file not found.")
        return

    try:
        config = handle_config("load", config_path)
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        return

    config_temp.chat_model = config.get("chat_model_used")
    config_temp.instruct_model = config.get("instruct_model_used")
    config_temp.code_model = config.get("code_model_used")
    config_temp.max_memory_usage = config.get("maximum_memory_usage")

    if not check_model_paths([config_temp.chat_model, config_temp.instruct_model, config_temp.code_model]):
        logger.error("Model path check failed.")
        return

    try:
        launch_gradio_interface()
    except Exception as e:
        logger.error(f"Failed to launch interface: {e}")

if __name__ == "__main__":
    main()
