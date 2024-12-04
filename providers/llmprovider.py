
from enum import Enum
from providers.openai import OpenAIProvider
from providers.gemini import GeminiProvider
class ProviderSelector(Enum):
    OPENAI = "OpenAI"
    GEMINI = "Gemini"

class LLMProvider:
    def __init__(self, provider: ProviderSelector):
        if not isinstance(provider, ProviderSelector):
            raise ValueError(f"Invalid provider: {provider}")
        self.provider = provider

    def completion(self, message):
        if self.provider == ProviderSelector.OPENAI:
            return OpenAIProvider().completion(message)
        elif self.provider == ProviderSelector.GEMINI:
            # Implementa aquí la lógica para el proveedor Gemini
            return GeminiProvider().completion(message)
        else:
            raise ValueError("Provider not found")