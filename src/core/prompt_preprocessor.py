from openai import AzureOpenAI
from src.config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_DEPLOYMENT, OPENAI_API_VERSION

client = AzureOpenAI(
    api_version=OPENAI_API_VERSION,
    azure_endpoint=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY,
)

class PromptPreprocessor:
    def __init__(self):
        pass

    def correct_text(self, prompt):
        """
        Corrige errores gramaticales y mejora la claridad del prompt usando Azure OpenAI.
        """
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Eres un asistente que corrige texto."},
                {"role": "user", "content": f"Corrige y mejora este texto:\n\n{prompt}"}
            ],
            max_tokens=200,
            temperature=0.7,
            model=OPENAI_DEPLOYMENT
        )
        return response.choices[0].message.content.strip()