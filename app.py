from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///albums.db"
db = SQLAlchemy(app)

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
        album_name = request.form["album_name"]
        new_album = Album(name=album_name)
        db.session.add(new_album)
        db.session.commit()
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)