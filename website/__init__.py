from flask import Flask
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    image = os.path.join('img')

    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = image
    app.config['SECRET_KEY'] = "Dylansstuff"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .view import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

     
    return app

    
