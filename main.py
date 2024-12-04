# /main.py
import os
from dotenv import load_dotenv

from core.website import Website
from core.prompts import Prompts
from providers.llmprovider import LLMProvider, ProviderSelector

load_dotenv()

provider = LLMProvider(ProviderSelector.GEMINI)
prompts = Prompts()

def summarize(url):
    website = Website(url)
    message = prompts.messages_for(website)
    return provider.completion(message)

print(summarize("https://alerodriguez.dev"))