# Album Tracker (tentative name)

## Description:
A personal website for reviewing music albums, similar to film review application, Letterboxd. Search Spotify's catalog of music for your favorite albums, choose them, and write your review

## Features:
- Search albums through Spotify API
- Rate albums using 1-5 scale including .5 increments, and write a personal review
- Timestamp when album is rated
- Delete album entries when user no longer wants them
- UI styled in Bootstrap dark theme

## Stack and Setup:
-**Backend:** Python, Flask, SQLAlchemy
-**Database:** SQLite
-**Frontend:** HTML, Jinja2, Bootstrap
-**External API:** Spotify API
-**Deployment:** Render with GitHub connection
### Installation:
**Requirements:** Python 3.10+ and Spotify Developer account
1. Clone the repo:
git clone https://github.com/yourusername/album-tracker.git
cd album-tracker
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate
3. Install dependencies:
pip install -r requirements.txt
4. Create .env file with your Spotify credentials:
SPOTIFY_CLIENT_ID=your_id
SPOTIFY_CLIENT_SECRET=your_secret
5.Run app:
python app.py
6. Visit locally in your browser:


