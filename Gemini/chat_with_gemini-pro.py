import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load OpenAI API Key from .env file
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Create the Model
model = genai.GenerativeModel('gemini-pro')

# Initialize the chat
chat = model.start_chat(history=[])

# Create a loop for contineous chat with Gemini and break when user type "quit"
while True:
    user_prompt = input("\nYou: ")
    if user_prompt == "quit":
        break
        
    response = chat.send_message(user_prompt)
    print("Gemani: " + str(response.text))
