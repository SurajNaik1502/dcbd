import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCXS8cqy_sJSRRjAh5rW9Q1sToqigK_5Nw")

# Define the prompt template
prompt_template = """ 
You are a creative AI specializing in generating highly detailed, vivid, and imaginative visual prompts. Your task is to craft a highly descriptive and immersive scene based on the following idea:

    Concept: {user_prompt}

Ensure that the description:
- Contains rich sensory details (sight, sound, texture, lighting, atmosphere).
- Specifies key visual elements, such as characters, objects, environments, colors, and emotions.
- Uses evocative language to create a strong mental image.
- Is structured in a way that an AI image generator can interpret effectively.

Keep the description between 10 to 20 words, making it as detailed and clear as possible.
"""
def generate_visual_prompt(user_prompt):
    formatted_prompt = prompt_template.format(user_prompt=user_prompt)
    
    model = genai.GenerativeModel("gemini-2.0-flash")  # Use "gemini-pro" or "gemini-pro-vision" as needed
    response = model.generate_content(formatted_prompt)
    
    return response.text  # Ensure this works correctly

if __name__ == "__main__":
    user_prompt = "Leo, king of this golden realm, lay sprawled beneath an acacia tree, his magnificent mane a rumpled halo."
    generated_prompt = generate_visual_prompt(user_prompt)
    print("Generated Visual Prompt:")
    print(generated_prompt)
