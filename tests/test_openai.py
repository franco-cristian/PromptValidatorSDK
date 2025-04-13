import unittest
from src.core.response_generator import ResponseGenerator

class TestOpenAIModel(unittest.TestCase):
    def test_openai_response(self):
        """
        Prueba si OpenAI responde correctamente.
        """
        generator = ResponseGenerator()
        response = generator.generate_response("¿Cuáles son los beneficios de la IA?")
        self.assertTrue(isinstance(response, str) and len(response) > 0)

if __name__ == "__main__":
    unittest.main()