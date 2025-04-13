from azure.cosmos import CosmosClient
import uuid
from src.config import COSMOS_DB_URI, COSMOS_DB_KEY, COSMOS_DB_DATABASE, COSMOS_DB_CONTAINER

class CosmosDBManager:
    def __init__(self):
        # Configuración del cliente Cosmos
        self.client = CosmosClient(COSMOS_DB_URI, credential=COSMOS_DB_KEY)
        self.database = self.client.get_database_client(COSMOS_DB_DATABASE)
        self.container = self.database.get_container_client(COSMOS_DB_CONTAINER)

    def save_record(self, prompt, response):
        """
        Almacena un registro en Cosmos DB.
        """
        try:
            # Crear un documento con un ID único
            document = {
                "id": str(uuid.uuid4()),  # ID único
                "prompt": prompt,
                "response": response
            }
            self.container.create_item(body=document)  # Inserta el documento
            return True
        except Exception:
            return False