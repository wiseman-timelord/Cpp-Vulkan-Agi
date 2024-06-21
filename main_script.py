# main.py
from scripts.menu_display import display_main_menu, display_model_menu, display_processor_menu, get_user_selection, launch_gradio_interface
from scripts.model_interaction import get_model_list, select_model, initialize_model, setup_agents

def main():
    processors = ["CPU AMD", "CPU Intel", "GPU AMD", "GPU NVIDIA"]
    current_model = "None"
    current_processor = "None"
    selected_model = None
    selected_processor = None

    while True:
        display_main_menu(current_model, current_processor)
        main_selection = get_user_selection()

        if main_selection == '1':
            models = get_model_list()
            while not selected_model:
                display_model_menu(models)
                model_selection = get_user_selection()

                if model_selection == 'r':
                    models = get_model_list()
                elif model_selection == 'x':
                    selected_model = None
                    break
                else:
                    selected_model = select_model(models, model_selection)
                    if not selected_model:
                        print("Invalid selection. Please try again.")
                    else:
                        current_model = selected_model

        elif main_selection == '2':
            while not selected_processor:
                display_processor_menu(processors)
                processor_selection = get_user_selection()

                if processor_selection == 'x':
                    selected_processor = None
                    break
                else:
                    if processor_selection.isdigit() and 1 <= int(processor_selection) <= len(processors):
                        selected_processor = processors[int(processor_selection) - 1]
                        current_processor = selected_processor
                    else:
                        print("Invalid selection. Please try again.")

        elif main_selection == 'x':
            print("Exiting program.")
            exit(0)
        
        if selected_model and selected_processor:
            if "GPU AMD" in selected_processor:
                device = "directml"
            elif "GPU NVIDIA" in selected_processor:
                device = "cuda"
            else:
                device = "cpu"

            model, tokenizer, device = initialize_model(selected_model, device)
            agents = setup_agents(selected_model, device)
            launch_gradio_interface(agents, tokenizer, device)
            break

if __name__ == "__main__":
    main()
