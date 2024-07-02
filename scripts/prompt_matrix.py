# .\data\prompt_matrix.py

def generate_dynamic_prompt(agent_type, task_stage, task_details):
    """
    Generates a dynamic prompt based on agent type, task stage, and task details.

    Parameters:
    - agent_type: Type of the agent (e.g., 'AI-CHAT', 'AI-INST', 'AI-CODE').
    - task_stage: The current stage of the task (e.g., 'initial', 'processing').
    - task_details: A dictionary containing details about the task.

    Returns:
    - A formatted string representing the dynamic prompt.
    """
    system_prompt = f"### SYSTEM:\nYou are roleplaying as {agent_type}. Your duties are: {task_details['roles']}."
    input_prompt = f"### INPUT:\nTask Stage: {task_stage}\nTask Description: {task_details['description']}\n"
    further_instructions = task_details.get('instructions', '')

    return f"{system_prompt}\n{input_prompt}{further_instructions}"

# Example task details for different agents and stages
task_details_chat_initial = {
    "roles": "User Interaction and Information Gathering",
    "description": "Greet the user and ask for details about their project.",
    "instructions": "Ensure the conversation is friendly and engaging."
}

task_details_inst_processing = {
    "roles": "Text Processing and Summarization",
    "description": "Summarize the following document and highlight key points.",
    "instructions": "Ensure the summary is concise and captures all the main ideas."
}

task_details_code_coding = {
    "roles": "Code Generation and Bug Fixing",
    "description": "Write a function to sort an array using quicksort algorithm.",
    "instructions": "The code should be efficient and well-documented."
}

# Generate dynamic prompts for different scenarios
dynamic_prompts = {
    "AI-CHAT": {
        "initial": generate_dynamic_prompt("AI-CHAT", "initial", task_details_chat_initial),
        "follow_up": generate_dynamic_prompt("AI-CHAT", "follow_up", task_details_chat_initial),
        "project_details": generate_dynamic_prompt("AI-CHAT", "project_details", task_details_chat_initial)
    },
    "AI-INST": {
        "processing": generate_dynamic_prompt("AI-INST", "processing", task_details_inst_processing),
        "summarizing": generate_dynamic_prompt("AI-INST", "summarizing", task_details_inst_processing),
        "analyzing": generate_dynamic_prompt("AI-INST", "analyzing", task_details_inst_processing)
    },
    "AI-CODE": {
        "coding": generate_dynamic_prompt("AI-CODE", "coding", task_details_code_coding),
        "debugging": generate_dynamic_prompt("AI-CODE", "debugging", task_details_code_coding),
        "reviewing": generate_dynamic_prompt("AI-CODE", "reviewing", task_details_code_coding)
    }
}

# Example function to retrieve dynamic prompts based on agent and task stage
def get_dynamic_prompt(agent_type, task_stage):
    """
    Retrieves the dynamic prompt based on the agent type and task stage.

    Parameters:
    - agent_type: Type of the agent (e.g., 'AI-CHAT', 'AI-INST', 'AI-CODE').
    - task_stage: The current stage of the task (e.g., 'initial', 'processing').

    Returns:
    - A string representing the dynamic prompt.
    """
    return dynamic_prompts[agent_type][task_stage]

# Example usage
if __name__ == "__main__":
    # Print a sample prompt for AI-CHAT in the initial stage
    print(get_dynamic_prompt("AI-CHAT", "initial"))
