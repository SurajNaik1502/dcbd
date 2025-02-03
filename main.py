import random

# Define some generic conflict and resolution rules
conflicts = [
    "a terrible storm was approaching",
    "they were trapped and had to find a way out",
    "a hidden treasure was buried nearby",
    "an enemy was watching them from the shadows",
    "they were lost and needed to find their way back"
]

resolutions = [
    "they worked together and found a solution",
    "they used their intelligence to escape",
    "they learned to trust each other and succeeded",
    "they discovered an ancient secret that helped them"
]

# Function to generate a dynamic story
def generate_dynamic_story(prompt):
    words = prompt.lower().split(" and ")

    if len(words) != 2:
        return "Please provide a prompt in the format: 'Character1 and Character2'"

    char1, char2 = words
    
    # Guess a possible setting based on characters (basic logic)
    settings = {
        "mouse": "a dense jungle",
        "lion": "the vast savannah",
        "robot": "a futuristic city",
        "astronaut": "deep space",
        "pirate": "the high seas",
        "wizard": "a mystical land"
    }
    
    setting = settings.get(char1, settings.get(char2, "a mysterious place"))

    # Select a random conflict and resolution
    conflict = random.choice(conflicts)
    resolution = random.choice(resolutions)

    # Construct the story dynamically
    story = (
        f"Once upon a time, {char1.capitalize()} met {char2.capitalize()} in {setting}. "
        f"Suddenly, {conflict}. "
        f"But in the end, {resolution}."
    )
    
    return story

# Example Usage
user_prompt = "The Robot and the Astronaut"
print(generate_dynamic_story(user_prompt.lower()))
