from src.azure_prompt_sdk import AzurePromptSDK

sdk = AzurePromptSDK()

# Pedir el prompt al usuario
prompt = input("Ingresa tu prompt: ")

result = sdk.validate_prompt(prompt)

if result.get("status") == "approved":
    print("✅ Prompt corregido:", result.get("corrected_prompt"))
    print("🤖 Respuesta:", result.get("response"))
elif result.get("status") == "modified":
    print("⚠️ El prompt contenía contenido sensible.")
    print("🔄 Sugerencia segura:", result.get("safe_prompt"))
else:
    print("❌ Error:", result.get("message"))