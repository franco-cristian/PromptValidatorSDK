from fastapi import FastAPI
from src.azure_prompt_sdk import AzurePromptSDK

app = FastAPI()
sdk = AzurePromptSDK()

@app.post("/validate")
async def validate(prompt: str):
    """
    Endpoint para validar y generar respuesta para un prompt.
    """
    return sdk.validate_prompt(prompt)