# /main.py
import os
from dotenv import load_dotenv
from openai import OpenAI
from core.website import Website
from core.prompts import Prompts

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError('API key is missing')

openai = OpenAI()
prompts = Prompts()

def summarize(url):
    website = Website(url)
    message = prompts.messages_for(website)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=message
    )
    return response.choices[0].message.content

print(summarize("https://alerodriguez.dev"))