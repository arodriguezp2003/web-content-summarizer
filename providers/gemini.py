import os
import google.generativeai as genai

class GeminiProvider:
    model = None
    def __init__(self):
    
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Google Generative AI API key is missing")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        

    def completion(self, message):
        trx = self.transform_to_gemini(message)
        response = self.model.generate_content(trx)
        return response.text

    def transform_to_gemini(self, messages_chatgpt):
        messages_gemini = []
        system_promt = ''
        for message in messages_chatgpt:
            if message['role'] == 'system':
                system_promt = message['content']
            elif message['role'] == 'user':
                messages_gemini.append({'role': 'user', 'parts': [message['content']]})
            elif message['role'] == 'assistant':
                messages_gemini.append({'role': 'model', 'parts': [message['content']]})
        if system_promt:
            messages_gemini[0]['parts'].insert(0, f"*{system_promt}*")

        return messages_gemini