from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///albums.db"
db = SQLAlchemy(app)

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

def get_spotify_token():
    auth_response = requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "client_credentials"}, auth=(CLIENT_ID, CLIENT_SECRET))
    auth_data = auth_response.json()
    return auth_data["access_token"]

def search_album(query):
    results =[]
    token = get_spotify_token()
    headers = {'Authorization':f'Bearer {token}'}
    params = {'q': query,  'type':'album'}
    album_response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    album_data = album_response.json()
    for item in album_data['albums']['items']:
        album_name = item['name']
        artist_name = item['artists'][0]['name']
        album_info = {'name': album_name, 'artist': artist_name}
        results.append(album_info)
    return results

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    albums = Album.query.all()
    return render_template("home.html", albums=albums)

@app.route("/about")
def about():
    return "App created by music lovers for 'music lovers"

@app.route("/add", methods=["GET", "POST"])
def add_album():
    if request.method == "POST":
        query = request.form["album_name"]
        results = search_album(query)
        return render_template('add.html', results=results)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)