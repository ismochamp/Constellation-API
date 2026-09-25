"""
Configuration module - loads environment variables once at startup.

This avoids reading from os.getenv() on every request, which is a best practice
for performance and maintainability.

All required environment variables are validated at import time, so the application
fails fast with clear error messages if configuration is missing.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Default values
DEFAULT_FRONTEND_URL = "http://localhost:5173"

# Read configuration once at startup (not on every request)
 _API_URL = os.getenv(" _API_URL")
 _AUTH_URL = os.getenv(" _AUTH_URL")
 _CLIENT_ID = os.getenv(" _CLIENT_ID")
 _CLIENT_SECRET = os.getenv(" _CLIENT_SECRET")
FRONTEND_URL = os.getenv("FRONTEND_URL", DEFAULT_FRONTEND_URL)

# Validate required configuration at startup
_missing_vars = []

if not  _API_URL:
    _missing_vars.append(" _API_URL")
if not  _AUTH_URL:
    _missing_vars.append(" _AUTH_URL")
if not  _CLIENT_ID or  _CLIENT_ID == "your-client-id-here":
    _missing_vars.append(" _CLIENT_ID")
if not  _CLIENT_SECRET or  _CLIENT_SECRET == "your-client-secret-here":
    _missing_vars.append(" _CLIENT_SECRET")

if _missing_vars:
    raise ValueError(
        f"Missing or invalid required environment variables: {', '.join(_missing_vars)}. "
        f"Please check your backend/.env file."
    )
