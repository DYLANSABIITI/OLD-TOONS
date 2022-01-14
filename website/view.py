from flask import Blueprint, render_template, request, redirect, url_for
import os
from flask import Flask


search_icon = os.path.join('static','img')
ben_eps = os.path.join('Season 1')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = search_icon
app.config['BEN_10_FOLDER'] = ben_eps


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home", methods=['POST','GET'])
def home():
    search = os.path.join(app.config['UPLOAD_FOLDER'], 'search.png')
    bg = os.path.join(app.config['UPLOAD_FOLDER'], 'bg.jpg')
    cover = os.path.join(app.config['UPLOAD_FOLDER'], 'cover.png')
    ben_10_logo = os.path.join(app.config['UPLOAD_FOLDER'], 'ben_10_logo.jpeg')
    alien_force_logo = os.path.join(app.config['UPLOAD_FOLDER'], 'alien_force_logo.png')
    ultimate_alien = os.path.join(app.config['UPLOAD_FOLDER'], 'ultimate_alien.png')


    return render_template('home.html', search=search, ben_10_logo=ben_10_logo, alien_force_logo=alien_force_logo, ultimate_alien=ultimate_alien)

@views.route("/video")
def video():
    return render_template('video.html')