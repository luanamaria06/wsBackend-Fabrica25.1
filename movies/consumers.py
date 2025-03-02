import requests

OMDB_API_KEY = '9df9e131'

def get_movie_from_omdb(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    return response.json()


