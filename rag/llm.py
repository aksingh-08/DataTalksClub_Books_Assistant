from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI

from rag.config import MODEL_NAME, BASE_URL, MAX_COMPLETION_TOKENS

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError(
        'GITHUB_TOKEN not found. Please set it in your .env file.'
    )

client = OpenAI(
    api_key=GITHUB_TOKEN,
    base_url=BASE_URL
)

def generate_answer(prompt: str):
    '''
    Send a prompt to the LLM and return the generated text.
    '''
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'user',
                'content': prompt,
            }
        ],
        max_completion_tokens=MAX_COMPLETION_TOKENS,
        # temperature=TEMPERATURE
    )
    usage = response.usage
    
    return (
        response.choices[0].message.content,
        {
            "prompt_tokens": usage.prompt_tokens,
            "completion_tokens": usage.completion_tokens,
            "total_tokens": usage.total_tokens, 
        },
    )