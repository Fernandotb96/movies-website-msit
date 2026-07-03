import os
import dotenv
import requests

dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found. Please check your .env file.")

API_URL = "https://www.omdbapi.com/"


def fetch_movie_data(title):
    """Fetch movie information from the OMDb API by title."""
    params = {"apikey": API_KEY, "t": title}
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "True":
            return data
        return None
    except requests.RequestException as e:
        print(f"Error with the API: {e}")
        return None
