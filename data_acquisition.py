import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.profootballfocus.com"
API_KEY = os.environ["PFF_API_KEY"]
LEAGUE = "nfl"

def get_token():
    r = requests.post(
        f"{BASE_URL}/auth/login",
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
    )
    r.raise_for_status()
    data = r.json()
    return data["jwt"] if "jwt" in data else data["access_token"]

def get_plays(token, season):
    url = f"{BASE_URL}/v1/open_exchange/{LEAGUE}/{season}/plays"
    r = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
        params={"format": "json"},
    )
    r.raise_for_status()
    data = r.json()
    return data.get("plays", data if isinstance(data, list) else [])

def __main__():
    season = int(input("Which season would you like to obtain data for?:"))
