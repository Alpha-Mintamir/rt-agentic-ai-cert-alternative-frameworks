# lesson1_openai_sdk

This folder contains example scripts demonstrating how to use the OpenAI Python SDK for various tasks:

## Files

- `chat_completions.py`: Example of sending a chat completion request to OpenAI's API,  summarization prompts.
- `translation.py`: Example of translating sentense from English to French using chat completion API.
- `audio_transcription.py`: Example of transcribing audio using OpenAI's API.
- `text_embeddings.py`: Example of generating text embeddings using OpenAI's API.
- `requirements.txt`: Lists required Python packages for these scripts.

## Setup

1. (Recommended) Create a Python virtual environment:
    - **Linux/macOS:**
       ```bash
       python3 -m venv venv
       source venv/bin/activate
       ```
    - **Windows (Command Prompt):**
       ```cmd
       python -m venv venv
       venv\Scripts\activate
       ```
    - **Windows (PowerShell):**
       ```powershell
       python -m venv venv
       .\venv\Scripts\Activate.ps1
       ```

2. Create a `.env` file in this folder (or root folder) and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. If you want to use your own data (e.g., for audio transcription), place your files in the `data/` folder. Update script paths as needed.

## Usage

Run any script directly, e.g.:

```bash
python chat_completions.py
```

## Notes

- Make sure your API key is valid and you have access to the required OpenAI models.
- See each script for specific usage details and example prompts.
- The `data/` folder is intended for storing sample or user-provided files (such as audio for transcription). Create it if it does not exist.
