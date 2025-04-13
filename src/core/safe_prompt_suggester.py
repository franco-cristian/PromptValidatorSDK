import openai
from src.config import OPENAI_API_KEY, OPENAI_API_BASE

# Configuración global para la API de OpenAI
openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_API_BASE  # Establecer el base URL aquí

class SafePromptSuggester:
    def __init__(self):
        pass

    def suggest_safe_prompt(self, prompt, issues):
        response = openai.chat.completions.create(  # Corregir la llamada a chat.completions.create()
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente que sugiere prompts seguros."},
                {"role": "user", "content": f"El siguiente texto contiene lenguaje sensible o dañino ({', '.join(issues)}). Reescríbelo de manera segura y ética:\n\n{prompt}"}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"].strip()