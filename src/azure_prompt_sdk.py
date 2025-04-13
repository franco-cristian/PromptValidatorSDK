from src.core.prompt_preprocessor import PromptPreprocessor
from src.core.content_validator import ContentValidator
from src.core.safe_prompt_suggester import SafePromptSuggester
from src.core.response_generator import ResponseGenerator
from src.services.cosmosdb_manager import CosmosDBManager

class AzurePromptSDK:
    def __init__(self):
        self.preprocessor = PromptPreprocessor()
        self.validator = ContentValidator()
        self.suggester = SafePromptSuggester()
        self.generator = ResponseGenerator()
        self.storage = CosmosDBManager()

    def validate_prompt(self, prompt):
        print("🛡️ Validando contenido en Content Safety...")

        validation = self.validator.validate(prompt)

        if not validation["is_safe"]:
            return {
                "status": "rejected",
                "message": validation["message"],
                "issues": validation["issues"]
            }

        print("✍️ Corrigiendo gramática y claridad...")
        corrected_prompt = self.preprocessor.correct_text(prompt)

        print("🤖 Generando respuesta con GPT-4o...")
        response = self.generator.generate_response(corrected_prompt)

        print("💾 Guardando en Cosmos DB...")
        self.storage.save_record(prompt, {"corrected_prompt": corrected_prompt, "response": response})

        return {
            "status": "approved",
            "corrected_prompt": corrected_prompt,
            "response": response
        }