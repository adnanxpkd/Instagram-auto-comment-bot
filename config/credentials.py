import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
TARGET_POST_URL = os.getenv("TARGET_POST_URL")

if not USERNAME or not PASSWORD:
    raise ValueError("Instagram credentials not found in .env file.")
if not TARGET_POST_URL:
    raise ValueError("TARGET_POST_URL not set in .env file.")
