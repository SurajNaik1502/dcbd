import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load model
model_name = "gpt2"  
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.eos_token

device = torch.device("cpu")  # Set to CPU to avoid GPU memory issues
model.to(device)

def generate_story(prompt, max_length=200, temperature=0.7, top_p=0.9):
    """
    Generates a short story using GPT-2 based on the given prompt.
    
    Parameters:
        prompt (str): The initial text input from the user.
        max_length (int): The maximum number of tokens in the generated story.
        temperature (float): Controls randomness (higher = more random, lower = more predictable).
        top_p (float): Nucleus sampling parameter (higher = more diverse output).
    
    Returns:
        str: Generated story text.
    """
    
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    attention_mask = torch.ones(input_ids.shape, dtype=torch.long).to(device)

    # Generate story text
    with torch.no_grad():
        output = model.generate(
            input_ids, 
            attention_mask=attention_mask,  # Pass attention mask
            max_length=max_length, 
            temperature=temperature, 
            top_p=top_p, 
            do_sample=True,  # randomness
            pad_token_id=tokenizer.pad_token_id  # Use pad_token_id explicitly
        )

    story = tokenizer.decode(output[0], skip_special_tokens=True)
    return story

if __name__ == "__main__":
    user_prompt = input("Enter a story prompt: ")
    generated_story = generate_story(user_prompt)
    print("\nGenerated Story:\n", generated_story)

# https://www.webtoons.com/en/action/boundless-ascension/episode-84/viewer?title_no=5228&episode_no=84