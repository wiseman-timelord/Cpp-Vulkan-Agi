# .\model_interaction.py

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Tuple

def initialize_model(model_name, device):
    if device == "directml":
        import torch_directml
        dml = torch_directml.device()
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto").to(dml)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer, dml
    else:
        # Assuming AVX2 optimizations are utilized by default on the CPU
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer, device

def generate_response(agent, tokenizer, device, user_input, chat_history):
    prompt = "You are a helpful assistant."
    messages = [{"role": "system", "content": prompt}] + [{'role': 'user', 'content': msg[0]} for msg in chat_history]
    messages.append({'role': 'user', 'content': user_input})
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    generated_ids = agent.generate(model_inputs.input_ids, max_new_tokens=512)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    chat_history.append((user_input, response))
    return chat_history
