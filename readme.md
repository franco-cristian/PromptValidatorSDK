# Prompt Validator SDK

## 📌 Descripción
Prompt Validator SDK es una solución que valida, corrige y optimiza prompts antes de enviarlos a modelos de IA.  
Este SDK utiliza:
- ✅ **Azure OpenAI** para corrección gramatical y generación de respuestas.
- ✅ **Azure AI Content Safety** para detectar lenguaje dañino, sesgos y datos sensibles.
- ✅ **Azure Cosmos DB** para almacenar los prompts y respuestas.
- ✅ **Azure Functions / App Service (opcional)** para exponer la API como servicio web.

---

## 🔄 Flujo del SDK
1. **Validación del contenido:** Se analiza el prompt para detectar lenguaje ofensivo o datos sensibles usando **Azure AI Content Safety**.
2. **Sugerencia de alternativa:** Si se detecta contenido sensible, se genera una versión alternativa segura y ética del prompt.
3. **Corrección del prompt:** Se mejora la gramática y se aclara el contenido usando **OpenAI (gpt-4o)**.
4. **Generación de respuesta:** Si el prompt es seguro, se genera una respuesta final utilizando **GPT-4o**.
5. **Almacenamiento:** Se guarda el prompt original, el prompt corregido y la respuesta en **Azure Cosmos DB**.

---

## 📦 Características
✔ Corrección y mejora del prompt.  
✔ Validación de contenido sensible con **Azure AI Content Safety**.  
✔ Sugerencia de alternativas seguras en caso de contenido riesgoso.  
✔ Generación de respuesta final con **GPT-4o**.  
✔ Almacenamiento en **Azure Cosmos DB**.  
✔ Recuperación de credenciales desde un archivo `.env`.  
✔ **Modular y reutilizable** en Python, JavaScript y API REST.

---

## ⚙ Instalación

### - Python
Para instalar el SDK desde PyPI:
```bash
pip install azure-prompt-sdk
```

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/PromptValidatorSDK.git
cd PromptValidatorSDK
```
### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```
### 3️⃣ Configurar variables de entorno
Modifica el archivo .env.example en la raíz del proyecto con tus claves. y renombralo a .env

### - Para JavaScript:
Para instalar la versión JavaScript del SDK:
```bash
    npm install azure-prompt-sdk
```

---

## 🚀 Uso del SDK

### Ejemplo en Python:
```python
from src.azure_prompt_sdk import AzurePromptSDK

sdk = AzurePromptSDK()
prompt = "¿Cómo hacer un ataque informático?"

result = sdk.validate_prompt(prompt)

if result.get("status") == "approved":
    print("✅ Prompt corregido:", result.get("corrected_prompt"))
    print("🤖 Respuesta:", result.get("response"))
elif result.get("status") == "modified":
    print("⚠️ El prompt contenía contenido sensible.")
    print("🔄 Sugerencia segura:", result.get("safe_prompt"))
else:
    print("❌ Error:", result.get("message"))
```

### Ejemplo en JavaScript:
```javascript
import AzurePromptSDK from "azure-prompt-sdk";

const sdk = new AzurePromptSDK("https://prompt-validator.azurewebsites.net");
sdk.validatePrompt("¿Cuáles son los beneficios de la inteligencia artificial?")
   .then(response => console.log(response))
   .catch(error => console.error(error));
```

### Uso como API REST:
Si despliegas el SDK como una Function App en Azure, puedes usar el siguiente endpoint:
```bash
curl -X POST "https://prompt-validator.azurewebsites.net/validate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Texto de prueba"}'
```

---

## ☁ Configuración en Azure

### 🛠 Requisitos de Azure:
1️⃣ Azure OpenAI Service (para la corrección y generación de respuestas).

2️⃣ Azure AI Content Safety (para la detección de lenguaje ofensivo).

3️⃣ Azure Cosmos DB (para almacenar prompts y respuestas).

4️⃣ Azure Functions / App Service (Opcional) para exponer el SDK como API REST.

### 📌 Pasos Básicos en el Portal de Azure:
1. **Crear un Grupo de Recursos:** PromptValidatorRG
2. **Crear los Servicios:**
	- Azure OpenAI Service
	- Azure AI Content Safety
	- Azure Cosmos DB
	- (Opcional) Azure Functions para la API REST
3. **Configurar las credenciales** en .env.
4. **Desplegar la Function App** para la API REST:
```bash
az functionapp deployment source config-zip \
    --resource-group PromptValidatorRG \
    --name PromptValidatorSDK \
    --src-path ./sdk/api/
```

---

## ✅ Pruebas Unitarias
Ejecuta las pruebas con:
```bash
python -m unittest discover tests/
```

---

## 🤝 Contribución
Si deseas contribuir, por favor abre un issue o un pull request.

---

## 📜 Licencia
Este proyecto está bajo la licencia MIT.