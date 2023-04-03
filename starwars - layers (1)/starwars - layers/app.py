import os
from flask import Flask
import requests

from flask import jsonify

print("Application startup")
#port = int(os.environ['PORT'])

port = 3000
print("PORT::", port)

app = Flask(__name__)

movie_url = "https://swapi.dev/api/films"
# "https://swapi.dev/api/films/"


@app.route("/", methods=['GET'])
def list_movies():
    data = requests.get(movie_url).json()
    movies = [{"id": people["episode_id"], "name": people["tittle"]} for people in data["results"]]
    charcs = [{people["characters"]} for people in data["results"]]
    return jsonify(movies)
def list_chars(url):
    data = requests.get(url).json()
    charcs = [{people["characters"]} for people in data["results"]]
    return jsonify(charcs)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
