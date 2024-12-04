import os
from openai import OpenAI

class OpenAIProvider:
    openai : OpenAI
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError('API key is missing')
        self.openai = OpenAI()

    def completion(self, message):
        response = self.openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=message
        )
        return response.choices[0].message.content