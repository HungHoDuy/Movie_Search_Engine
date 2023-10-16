import requests # the lib that handles the url stuff
import json

def poster_find(movie_id):
    movie_id=19
    target_ur = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c2c3992b8ca4966ce0e58aa69429fafe"
    resp = requests.get(target_ur)
    if resp.status_code == 200:
        resp_json = json.loads(resp.text)
        poster_path = 'https://image.tmdb.org/t/p/original/'+ resp_json['poster_path']
    return poster_path

# print(poster_find(921))