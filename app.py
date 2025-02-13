import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the DeepSeek model and tokenizer
model_name = "deepseek-ai/deepseek-llm-7b-chat"  # Using DeepSeek-LLM-7B
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float16,  # Use half precision for better performance
    device_map="auto",  # Auto-assign devices (GPU/CPU)
    offload_folder="offload"  # Set a folder to offload model weights
)

# Ensure the tokenizer has a pad token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Function to generate a story from a prompt
def generate_story(prompt, max_length=300, temperature=0.7, top_p=0.9):
    input_ids = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).input_ids.to(model.device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id
        )

    story = tokenizer.decode(output[0], skip_special_tokens=True)
    return story

# Example Usage
if __name__ == "__main__":
    user_prompt = input("Enter a story prompt: ")
    generated_story = generate_story(user_prompt)
    print("\nGenerated Story:\n", generated_story)
