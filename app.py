from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime, timezone

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
        image_url = item['images'][0]['url']
        album_info = {'name': album_name, 'artist': artist_name, 'image_url': image_url}
        results.append(album_info)
    return results

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    review = db.Column(db.String(5000),nullable=True)
    date_logged = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    image = db.Column(db.String(300), nullable=True)

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
        if "search_query" in request.form:
            query = request.form["search_query"]
            results = search_album(query)
            return render_template('add.html', results=results)
        elif "album_name" in request.form:
            album_name = request.form["album_name"]
            artist_name = request.form["artist_name"]
            rating = float(request.form['rating'])
            review = request.form['review']
            image_url = request.form['album_image']
            new_album = Album(name=album_name, artist= artist_name, rating=rating, review=review, image=image_url)
            db.session.add(new_album)
            db.session.commit()
    return render_template("add.html")

@app.route('/delete', methods=['POST'])
def delete_album():
    album_id = request.form['album_id']
    album = Album.query.get(album_id)
    db.session.delete(album)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)