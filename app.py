# app.py
from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

# Dummy data for images
photos = [
    {'filename': 'gala.jpg', 'focused_couple': 'Alice & Bob', 'random_couple': False},
    {'filename': 'couple.jpg', 'focused_couple': '', 'random_couple': True},
    {'filename': 'zee.jpg', 'focused_couple': 'Zee', 'random_couple': False},
    {'filename': 'date_night.jpg', 'focused_couple': '', 'random_couple': True},
    {'filename': 'able-chungu.jpg', 'focused_couple': '', 'random_couple': False},
    {'filename': 'neo-slay.jpg', 'focused_couple': '', 'random_couple': False},
]

@app.route('/')
def landing():
    return render_template('landing.html')
@app.route('/constitution')
def constitution():
    return render_template('constitution.html')

@app.route('/dashboard')
def dashboard():
    current_year = datetime.now().year
    return render_template('dashboard.html', current_year=current_year)

@app.route('/gala_photos')
def gala_photos():
    current_year = datetime.now().year
    return render_template('gala_photos.html', photos=photos, current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True)