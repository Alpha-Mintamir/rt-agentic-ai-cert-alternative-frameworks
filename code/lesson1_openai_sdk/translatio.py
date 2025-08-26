# Step 1: Import libraries

from openai import OpenAI
import os
from dotenv import load_dotenv

# Step 2: Load the API key from .env and pass it to the OpenAI object to authorize the request

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# Step 3: Send a chat completion request to translate a text and print the response

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful translation assistant."},
        {"role": "user", "content": """Translate the following text into French:

        "The meeting has been moved to Friday. Please prepare your slides by Thursday evening."
        """}
    ]
)

print(response.choices[0].message.content)
