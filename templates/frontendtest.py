from flask import Flask, request, jsonify, render_template
import keys
import openai
from openai import OpenAI
from pydantic import BaseModel
from typing import List

app = Flask(__name__)

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

# Web version of output_function and input_function
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']
    
    # Process user input and update message history
    if user_input.isdigit():
        choice_index = int(user_input) - 1
        last_response = message_history[-1]["content"]
        
        if "Options" in last_response:
            options = last_response.split("\nOptions: ")[1].split(", ")
            if 0 <= choice_index < len(options):
                message_history.append({"role": "user", "content": options[choice_index]})
            else:
                return jsonify({"error": "Invalid choice. Please select a valid option."})
        else:
            return jsonify({"error": "No options available."})
    else:
        message_history.append({"role": "user", "content": user_input})

    # Get the response from the narrator
    response_text = get_narrator_response(message_history)

    # Check for end of game or an error
    if isinstance(response_text, str):
        return jsonify({"story": response_text, "game_end": True})
    elif response_text.story_end:
        return jsonify({"story": response_text.story, "game_end": True})

    return jsonify({
        "story": response_text.story,
        "question": response_text.question,
        "options": response_text.options,
        "game_end": response_text.story_end
    })

if __name__ == "__main__":
    app.run(debug=True)