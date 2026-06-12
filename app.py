# app.py
from flask import Flask, render_template, url_for, send_from_directory
from datetime import datetime
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Dummy data for images
photos = [
    {'filename': 'couple.jpg', 'focused_couple': 'N&M', 'random_couple': True},
    {'filename': 'gala 3.jpg', 'focused_couple': 'Stanely and the Team', 'random_couple': False},
    {'filename': 'gala 2.jpg', 'single_gent': 'Single Gent', 'random_couple': True},
    {'filename': 'able-chungu.jpg', 'Motivational_Speaker': 'Able Chungu', 'Special_Guest': True},
    {'filename': 'neo-slayer.jpg', 'Main_MC': 'Neo Slayer', 'Special_Guest': True},
]

@app.route('/')
def landing():
    return render_template('landing.html')
@app.route('/constitution')
def constitution():
    return render_template('constitution.html')

@app.route('/advert')
def advert():
    return render_template('advert.html')

@app.route('/dashboard')
def dashboard():
    current_year = datetime.now().year
    return render_template('dashboard.html', current_year=current_year)

@app.route('/gala_photos')
def gala_photos():
    current_year = datetime.now().year
    return render_template('gala_photos.html', photos=photos, current_year=current_year)

@app.route('/gala_inspiration')
def gala_inspiration():
    current_year = datetime.now().year
    return render_template('gala_inspiration.html', current_year=current_year)

@app.route('/gala_video')
def gala_video():
    current_year = datetime.now().year
    return render_template('gala_video.html', current_year=current_year)

@app.route('/blank_screen')
def blank_screen():
    return render_template('blank_screen.html')

@app.route('/video/gala1')
def serve_gala_video():
    video_path = os.path.join(app.root_path, 'static', 'images', 'gala 1.mp4')
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'), 'gala 1.mp4')

if __name__ == '__main__':
    app.run(debug=True)