from baml_client import b
from baml_client import reset_baml_env_vars
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Reset BAML environment variables
reset_baml_env_vars(dict(os.environ))

# Verify the API key is loaded
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError("OPENAI_API_KEY not found in environment variables")
