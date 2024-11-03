import keys
import openai
from openai import OpenAI
from pydantic import BaseModel
from typing import List

# Define the adventure game prompt to initialize the AI's context
intro_prompt = """
You are the narrator of a text-based adventure game set in a spaceship, inspired by the atmosphere of the movie Alien.
The player has just woken up alone on a mysterious spaceship and must navigate this dangerous environment. 
Each response you provide should follow this structure:

Story: A descriptive narrative that immerses the player in the current moment.
Question: A prompt inviting the player to make a decision or ask a question.
Options: Three clear, numbered choices for the player to select from.
Story_end: A boolean indicating if the story has reached an ending. True if the story has ended, False otherwise.

The player can either ask a question to gather more information or make a decision to move the story forward. 
If they ask a question, give them only the relevant information within the story’s context and then repeat the last question you posed, waiting for them to make a choice. 
When they make a decision, update the story accordingly and provide a new question with three options to guide their next steps.

The game should have a maximum of five decision points, leading to various possible endings based on the player's choices. 
Ensure that the story evolves uniquely depending on their choices.

Each time, the option should start by 1. 2. 3. and the player can choose one of the options by typing the number of the option.
"""

# modify for front end 
def output_function(output):
    print(output)

def input_function():
    return input("Your choice or question: ")

# Define a model for the response structure
class NarratorResponse(BaseModel):
    story: str
    question: str
    options: List[str]
    story_end: bool

# a function that takes str, str, list[str], bool, and convert them into one string
def to_string(story, question, options, story_end):
    return f"Story: {story}\nQuestion: {question}\nOptions: {', '.join(options)}\nStory_end: {story_end}"
    
# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key=keys.KEY
)

# Initialize the message history with the introduction prompt
message_history = [
    {"role": "system", "content": intro_prompt}
]

def get_narrator_response(message_history):
    complition = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=message_history,
        response_format = NarratorResponse,
    )
    content = complition.choices[0].message.parsed

    message_history.append({"role": "system", "content": to_string(content.story, content.question, content.options, content.story_end)})
    return content

def play_game():
    output_function("Welcome to the Space Adventure!")
    output_function("You can type a number to make a choice or type a question to gather more information.")
 

    while True:
        response_text = get_narrator_response(message_history)
        # different cases of response_text
        # 1. if response_text is in the form of NarratorResponse use output_function to display the story, question, and options
        # 2. if response_text is an error message, display the error message and break the loop
        # 3. if response_text.story_end is True then break the loop and end the game

        # if response_text is an error message
        if isinstance(response_text, str):
            output_function(response_text)
            break

        if response_text.story_end:
            output_function(response_text.story)
            break
        else:
            output_function(response_text.story)
            output_function(response_text.question)
            for i, option in enumerate(response_text.options):
                output_function(f"{i+1}. {option}")

        user_input = input_function()
        # different cases of user_input
        # 1. if user_input is a number, add the user's choice to the message_history
        # 2. if user_input is a question, add the user's question to the message_history
        # 3. if user_input is neither a number nor a question, display an error message and continue the loop

        if user_input.isdigit():
            choice_index = int(user_input) - 1
            if 0 <= choice_index < len(response_text.options):
                message_history.append({"role": "user", "content": response_text.options[choice_index]})
            else:
                output_function("Invalid choice. Please select a valid option.")
        else:
            message_history.append({"role": "user", "content": user_input})

if __name__ == "__main__":

    play_game()

