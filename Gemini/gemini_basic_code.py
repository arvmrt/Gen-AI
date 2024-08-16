import os
from dotenv import load_dotenv
import google.generativeai as genai

# Define your prompt with question
prompt = "Who is the first president of USA?"

# Load OpenAI API Key from .env file
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Create the Model
model = genai.GenerativeModel('gemini-pro')

# Send the prompt to model and capture output in "response" variable
response = model.generate_content(prompt)    

# Print the output value
print(response.text)
