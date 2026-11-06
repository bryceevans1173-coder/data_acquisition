import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.profootballfocus.com"
API_KEY = os.environ["PFF_API_KEY"]
LEAGUE = "nfl"
SEASON = 2024

def get_token() -> str:
    """Step 1: exchange API key for a short-lived JWT."""
    r = requests.post(
        f"{BASE_URL}/auth/login",
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
    )
    r.raise_for_status()
    data = r.json()
    return data["jwt"] if "jwt" in data else data["access_token"]