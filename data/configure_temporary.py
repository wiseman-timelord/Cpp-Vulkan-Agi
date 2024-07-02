# .\data\configure_temporary.py

# Global Variables
project_planner = {
    "current_project_plan": "Project Plan:\n1. Get details of new project for the session.",
    "current_task_assigned": "Current Task:\nCommunicate with user, find out the details of the project.",
}
model_settings = {
    "chat_model": None,
    "instruct_model": None,
    "code_model": None,
}
memory_settings = {
    "max_memory_usage": 90,
}
dynamic_prompts = {
    "AI-CHAT": "Default prompt for AI-CHAT",
    "AI-INST": "Default prompt for AI-INST",
    "AI-CODE": "Default prompt for AI-CODE"
}
agent_states = {
    "AI-CHAT": "active",
    "AI-INST": "inactive",
    "AI-CODE": "active"
}
