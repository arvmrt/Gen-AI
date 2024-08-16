import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load OpenAI API Key from .env file
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Create the Model
model = genai.GenerativeModel('gemini-pro')

# Create a variable containing previous chat history. Note below format is must else it will give error.
chat_history = [
   {
      'role': 'user',
      'parts': ['Who is the first president of USA']
   },
   {
      'role': 'model',
      'parts': ['George Washington']
   }
]

# Initialize the chat
chat = model.start_chat(history=chat_history)

# Now ask a question with context of the previouly given history 
response = chat.send_message("and who is 16th ?")
print(response.text)
