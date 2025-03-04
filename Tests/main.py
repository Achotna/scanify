from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API
api_key = os.getenv("ANTHROPIC_API_KEY")
