# Step 1: Import libraries

from openai import OpenAI
import os
from dotenv import load_dotenv

# Step 2: Load the api key from .env and pass to the OpenAI object to authorize the request

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# Step 3: Send a chat completion request and print the summarized response

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": """Summarize this Slack thread:

        - John: Can we push the deadline? I'm swamped.
        - Priya: Maybe Monday?
        - Alex: Docs are 80% ready, just need final edits.
        - Sarah: I’ll handle the charts.
        - Priya: Friday might be better so everyone has the weekend free.
        - John: Friday works. Thanks.
        """}
    ]
)

print(response.choices[0].message.content)
