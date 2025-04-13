import unittest
from unittest.mock import patch, MagicMock
from src.azure_prompt_sdk import AzurePromptSDK

class TestAzurePromptSDK(unittest.TestCase):
    @patch("src.core.content_validator.ContentValidator.validate")
    @patch("src.core.prompt_preprocessor.PromptPreprocessor.correct_text")
    @patch("src.core.response_generator.ResponseGenerator.generate_response")
    @patch("src.services.cosmosdb_manager.CosmosDBManager.save_record")
    def test_validate_prompt(self, mock_save_record, mock_generate_response, mock_correct_text, mock_validate):
        """
        Prueba la validación, corrección y generación de respuesta en el SDK.
        """
        mock_validate.return_value = {"is_safe": True, "issues": []}
        mock_correct_text.return_value = "Prompt corregido."
        mock_generate_response.return_value = "Respuesta generada."
        mock_save_record.return_value = True

        sdk = AzurePromptSDK()
        result = sdk.validate_prompt("Ejemplo de prompt.")

        self.assertEqual(result["status"], "approved")
        self.assertEqual(result["corrected_prompt"], "Prompt corregido.")
        self.assertEqual(result["response"], "Respuesta generada.")

if __name__ == "__main__":
    unittest.main()