# Album Tracker (tentative name)

## Description:
A personal website for reviewing music albums, similar to film review application, Letterboxd. Search Spotify's catalog of music for your favorite albums, choose them, and write your review

## Features:
- Search albums through Spotify API
- Rate albums using 1-5 scale including .5 increments, and write a personal review
- Timestamp when album is rated
- Delete album entries when user no longer wants them
- UI styled in Bootstrap dark theme

## Tech Stack:
- **Backend:**
  - Python
  - Flask
  - SQLAlchemy

- **Database:**
  - SQLite

- **Frontend:**
  - HTML
  - Jinja2
  - Bootstrap

- **External API:**
  - Spotify API

- **Deployment:**
  - Render with GitHub connection

## Installation:
**Requirements:** Python 3.10+ and Spotify Developer account
### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/album-tracker.git
cd album-tracker
```
### 2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate
```
### 3. Install dependencies:
```
pip install -r requirements.txt
```
### 4. Create .env file with your Spotify credentials:
```
SPOTIFY_CLIENT_ID=your_id
SPOTIFY_CLIENT_SECRET=your_secret
```
### 5. Run app:
```
python app.py
```
### 6. Visit locally in your browser

## Usage
- Upon landing on the homepage, click add in the navbar at the top to be transported to the add page
- On the add page, search for an album on in the search bar, pressing the search album button for albums to appear.
- Pick an album, add a rating and optional review and click add this album.
- To view collection of reviews, go back to the home page.
- Delete reviews if desired.

## Roadmap:
- User authentication, perhaps involving the Spotify API, so that people can make accounts or login with Spotify account, and to allow multiple user usage
- Sorting/filtering when viewing personal collection of reviews, perhaps by date reviewed, and album info (genre, artist, etc)
- Edit button for existing entries, Relisten button for full relisten sessions of albums in the review section on the add page
- Fix for duplicate submission bug and bugs using browser arrows
- Fine tuned searching

## Project Status:
Developed as of September 2026 by Carlos Barahona Martell as a personal portfolio project. Development will slow down as I will be busy through the academic school year though I will try to make commitments.
