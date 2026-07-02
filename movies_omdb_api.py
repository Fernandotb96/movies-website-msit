import os
import dotenv
import requests

# Get API Key
dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")

API_URL = "https://www.omdbapi.com/"


def get_movie_from_api(title):
    """Fetches movie from OMDb API by title"""
    params = {"apikey": API_KEY, "t": title}
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if data["Response"] == "True":
            return data
        return None
    except Exception as e:
        print(f"Error with the API: {e}")
        return None
