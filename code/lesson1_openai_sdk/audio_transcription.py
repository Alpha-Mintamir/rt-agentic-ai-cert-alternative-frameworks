# Step 1: Import Libraries

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 2: Transcribe an audio file
with open("/home/alpha-lencho/ready-tensor/rt-agentic-ai-cert-module4-section1/data/meeting_clip.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

print(transcript.text)