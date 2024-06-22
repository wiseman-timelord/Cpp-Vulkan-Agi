# .\scripts\model_interaction.py

import ollama

def initialize_model(model_name, device):
    if device == "gpu":
        import torch_directml
        dml = torch_directml.device()
        model = ollama.chat(model=model_name, messages=[], device=dml)
        tokenizer = ollama.AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer, dml
    else:
        model = ollama.chat(model=model_name, messages=[])
        tokenizer = ollama.AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer, device

def generate_response(agent, tokenizer, device, user_input, chat_history):
    prompt = "You are a helpful assistant."
    messages = [{"role": "system", "content": prompt}] + [{'role': 'user', 'content': msg[0]} for msg in chat_history]
    messages.append({'role': 'user', 'content': user_input})
    response = ollama.chat(model=agent, messages=messages, device=device)
    chat_history.append((user_input, response['message']['content']))
    return chat_history
