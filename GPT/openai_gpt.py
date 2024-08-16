import os
from dotenv import load_dotenv
from openai import OpenAI

# Load OpenAI API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define your followup question
prompt = "Who is the first president of USA?."

# Initialize Model
client = OpenAI()

# Send prompt question and get response from Model
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",    
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    #temperature=0,                              # Optional
    #max_tokens=1,                               # Optional
    #response_format={ "type": "json_object" },  # Optional
)

#Extract only Answer from the Response
generated_text = chat_completion.choices[0].message.content
print(generated_text)

#Display Full Response
generated_text = chat_completion
print(generated_text)
