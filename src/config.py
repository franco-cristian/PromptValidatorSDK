import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Configuración de Azure OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "tu_api_key")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://tu_openai_endpoint.openai.azure.com")
OPENAI_DEPLOYMENT = os.getenv("OPENAI_DEPLOYMENT", "gpt-4o-mini")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION", "2024-12-01-preview")

# Configuración de Azure AI Content Safety
CONTENT_SAFETY_API_KEY = os.getenv("CONTENT_SAFETY_API_KEY", "tu_content_safety_api_key")
CONTENT_SAFETY_ENDPOINT = os.getenv("CONTENT_SAFETY_ENDPOINT", "https://tu_content_safety_endpoint.azure.com")

# Configuración de Azure Cosmos DB
COSMOS_DB_URI = os.getenv("COSMOS_DB_URI", "tu_cosmos_db_uri")
COSMOS_DB_KEY = os.getenv("COSMOS_DB_KEY", "tu_cosmos_db_key")
COSMOS_DB_DATABASE = os.getenv("COSMOS_DB_DATABASE", "tu_base_de_datos")
COSMOS_DB_CONTAINER = os.getenv("COSMOS_DB_CONTAINER", "tu_contenedor")