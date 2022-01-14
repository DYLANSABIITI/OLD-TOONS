from flask import Blueprint, render_template, request, redirect, session, Flask, url_for
import os
from flask import Flask

auth = Blueprint("auth", __name__)

search_icon = os.path.join('static','img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = search_icon


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)

    return render_template('LOGIN.html')


@auth.route("/sign-in", methods=["GET", "POST"])
def signin():
    bg = os.path.join(app.config['UPLOAD_FOLDER'], 'bg.jpg')

    return render_template('sign.html', bg=bg)


@auth.route("/sign-out")
def signout():

    return "USER HAS SIGNED OUT"