from openai import AzureOpenAI
from src.config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_DEPLOYMENT, OPENAI_API_VERSION

client = AzureOpenAI(
    api_version=OPENAI_API_VERSION,
    azure_endpoint=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY,
)

class ResponseGenerator:
    def __init__(self):
        pass

    def generate_response(self, prompt):
        """
        Genera una respuesta basada en el prompt optimizado usando Azure OpenAI.
        """
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Eres un asistente que genera respuestas basadas en prompts optimizados."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7,
            model=OPENAI_DEPLOYMENT
        )
        return response.choices[0].message.content.strip()