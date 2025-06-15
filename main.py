import requests
import base64
import os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Load .env file
load_dotenv()

# Step 1: Get credentials
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

if not client_id or not client_secret:
    print("❌ SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET is missing. Please check your .env file.")
    exit()

# Step 2: Get access token
def get_access_token():
    try:
        auth_str = f"{client_id}:{client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

        headers = {
            "Authorization": f"Basic {b64_auth_str}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
        if response.status_code != 200:
            print(f"❌ Failed to get access token. Status Code: {response.status_code}, Response: {response.text}")
            return None
        token = response.json().get("access_token")
        return token
    except Exception as e:
        print(f"❌ An error occurred while getting the access token: {e}")
        return None

# Step 3: Search song using lyrics
def search_song(lyrics):
    token = get_access_token()
    if not token:
        print("❌ Cannot search without a valid token.")
        return
    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }

        params = {
            "q": lyrics,
            "type": "track",
            "limit": 1
        }

        response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
        if response.status_code != 200:
            print(f"❌ Failed to search song. Status Code: {response.status_code}, Response: {response.text}")
            return

        result = response.json()
        track = result["tracks"]["items"][0]
        print("🎵 Song Name:", track["name"])
        print("🎤 Artist:", track["artists"][0]["name"])
        print("🔗 Spotify Link:", track["external_urls"]["spotify"])
    except IndexError:
        print("❌ No song found with those lyrics.")
    except Exception as e:
        print(f"❌ An error occurred while searching for the song: {e}")

# Example usage
if __name__ == "__main__":
    lyrics_input = input("Enter song lyrics: ")
    search_song(lyrics_input)