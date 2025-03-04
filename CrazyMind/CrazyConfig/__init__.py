import os
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file if it exists
if os.path.exists(".env"):
    logger.info("Loading .env file")
    load_dotenv(".env")

# Check if ENV environment variable is set or if .env file exists
use_env = os.environ.get("ENV", "False").lower() == "true" or os.path.exists(".env")

# Import configuration based on conditions
try:
    if use_env:
        logger.info("Loading configuration from sample_config.py")
        from sample_config import *  # noqa: F403
    elif os.path.exists("config.py"):
        logger.info("Loading configuration from config.py")
        from config import *  # noqa: F403
    else:
        raise ImportError("No configuration file found. Please ensure either 'sample_config.py' or 'config.py' exists.")
except ImportError as e:
    logger.error(f"Configuration import failed: {e}")
    raise
