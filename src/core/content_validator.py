import requests
import json
from src.config import CONTENT_SAFETY_API_KEY, CONTENT_SAFETY_ENDPOINT

class ContentValidator:
    def __init__(self):
        self.api_url = f"{CONTENT_SAFETY_ENDPOINT}/contentsafety/text:analyze?api-version=2023-10-01"
        self.headers = {
            "Ocp-Apim-Subscription-Key": CONTENT_SAFETY_API_KEY,
            "Content-Type": "application/json"
        }

    def validate(self, prompt):
        """
        Analiza el prompt usando Azure Content Safety.
        Si detecta contenido peligroso con severidad >= 2, se bloquea.
        """

        payload = {
            "text": prompt,
            "categories": ["Hate", "SelfHarm", "Sexual", "Violence"],
            "blocklistNames": [],
            "outputType": "FourSeverityLevels"
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)

        try:
            result = response.json()
        except json.JSONDecodeError:
            return {
                "is_safe": False,
                "message": "⛔ Error al analizar la respuesta de Azure Content Safety.",
                "issues": []
            }

        if "categoriesAnalysis" not in result:
            return {
                "is_safe": False,
                "message": "⛔ Error: La respuesta de Content Safety no contiene 'categoriesAnalysis'.",
                "issues": []
            }

        # Evaluar categorías y niveles de severidad
        flagged_categories = [
            category_data["category"]
            for category_data in result["categoriesAnalysis"]
            if category_data["severity"] >= 1  # 🚨 Umbral: Bloquear si severidad >= 2
        ]

        if flagged_categories:
            return {
                "is_safe": False,
                "message": "⛔ El prompt contiene contenido prohibido según Azure Content Safety.",
                "issues": flagged_categories
            }

        return {"is_safe": True, "issues": []}