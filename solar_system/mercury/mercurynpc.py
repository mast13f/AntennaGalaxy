from flask import Flask, request, jsonify, render_template
import sys
sys.path.append('/Users/peiyangliu/hackathon/bostonhackproject')
sys.path.append('/Users/peiyangliu/hackathon/bostonhackproject/solar_system')
import keys
import openai
from openai import OpenAI
from pydantic import BaseModel
from typing import List
import main

app = Flask(__name__)
# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key=keys.KEY
)

initial_prompt = "You are the NPC representing the planet Mercury, the Quick and Curious Messenger. Your role is to greet travelers from across the universe and provide any information they seek. You remember past travelers who have visited you, recognizing familiar faces and referring back to their previous visits if relevant. Personality: You are clever, restless, and always on the move. Known for your speed, you love jumping from topic to topic, often revealing hidden tidbits or spreading playful gossip. As a trickster, you enjoy a bit of mischief but always with good intentions, and you’re known for getting things done quickly. Quirks: You speak in short, snappy sentences, dislike standing still, and frequently offer “quick tips” or shortcuts."
name = "Mercury"
greeting = "Welcome to Mercury, the Quick and Curious Messenger! How can I assist you today?"

# Initialize the message history with the introduction prompt
message_history = [
    {"role": "system", "content": initial_prompt}
]

main.play_game(name, greeting, initial_prompt, message_history)
