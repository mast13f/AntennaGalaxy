import sys
sys.path.append('/Users/peiyangliu/hackathon/bostonhackproject')
import keys
import openai
from openai import OpenAI
from pydantic import BaseModel
from typing import List

# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key=keys.KEY
)

# Define a model for the response structure
class npcResponse(BaseModel):
    story: str
    story_end: bool

# modify for front end 
def output_function(output):
    print(output)

def input_function(text):
    return input(text)


# a function that takes str, str, list[str], bool, and convert them into one string
def to_string(story, story_end):
    return f"Story: {story}\nStory_end: {story_end}"

def get_npc_response(message_history):
    complition = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=message_history,
        response_format = npcResponse,
    )
    content = complition.choices[0].message.parsed

    message_history.append({"role": "system", "content": to_string(content.story,content.story_end)})
    return content

def play_game(planet, greeting, initial_prompt, message_history):
    output_function(greeting)
    output_function("You can talk about anything with me.")

    while True:
        response_text = get_npc_response(message_history)
        # different cases of response_text
        # 1. if response_text is in the form of npcResponse use output_function to display the story
        # 2. if response_text is an error message, display the error message and break the loop
        # 3. if response_text.story_end is True then break the loop and end the game

        # if response_text is an error message
        if isinstance(response_text, str):
            output_function(response_text)
            break

        if response_text.story_end:
            output_function(response_text.story)
            break

        if response_text.story:
            output_function(response_text.story)

        user_input = input_function("Say something to me: ")

        message_history.append({"role": "user", "content": user_input})





