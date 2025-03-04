import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
if os.path.exists(".env"):
    load_dotenv(".env")

# Check if ENV environment variable is set or if .env file exists
use_env = os.environ.get("ENV", "False").lower() == "true" or os.path.exists(".env")

# Import configuration based on conditions
if use_env:
    from sample_config import *  # noqa: F403
elif os.path.exists("config.py"):
    from config import *  # noqa: F403
else:
    raise ImportError("No configuration file found. Please ensure either 'sample_config.py' or 'config.py' exists.")
