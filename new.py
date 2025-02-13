import google.generativeai as genai
from gtts import gTTS
import os

genai.configure(api_key="AIzaSyCXS8cqy_sJSRRjAh5rW9Q1sToqigK_5Nw")

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_story(user_prompt):
    prompt_template = """You are an expert fantasy genre storyteller. Write a compelling, engaging, and imaginative story based on the following idea. Also use Indian names for characters and places.

    Story Idea: {user_prompt}

    Make sure the story has:
    - A captivating beginning that hooks the reader.
    - A well-structured middle with challenges and surprises.
    - A satisfying and creative ending.

    Write in a vivid, descriptive, and immersive style. Keep the language engaging and easy to understand.
    Limit the story to a maximum of 500 words.
    """

    prompt = prompt_template.format(user_prompt=user_prompt)
    response = model.generate_content(prompt, generation_config={"max_output_tokens": 1000})  
    return response.text

def text_to_speech(text, filename="story.mp3"):
    """Convert text to speech and save as an MP3 file."""
    tts = gTTS(text=text, lang="en", slow=False)  # Convert text to speech
    tts.save(filename)  # Save the audio file
    print(f"Audio saved as {filename}")
    os.system(f"start {filename}")  # Play the audio (works on Windows)

# Example usage
user_prompt = "Hero and demon"
story = generate_story(user_prompt)
print(story)

# Convert the generated story to speech
text_to_speech(story)
