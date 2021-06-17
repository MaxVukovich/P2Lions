from flask import Blueprint, render_template

from gamereview.Ahmad.bubblesort import bubble
from gamereview.Ahmad.calculator import Games
from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

gamereview_bp1 = Blueprint('gamereview1', __name__,
                           template_folder='templates',
                           static_folder='static', static_url_path='assets')

app = Flask(__name__)


@gamereview_bp1.route('/')
def index():
    return render_template("ahmadhome.html")

@gamereview_bp1.route('/games', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        k = int(request.form.get("series"))
        return render_template("games.html", gamerecs=Games(k))
    return render_template("games.html", gamerecs=Games(1))

@gamereview_bp1.route('/bubblesort', methods=['GET', 'POST'])
def bubbles():
    if request.form:
        return render_template("bubbles.html", sort=bubble(request.form.get("var")))
    return render_template("bubbles.html", sort=bubble("10,9,8,7,6,5,4,3,2,1"))

@gamereview_bp1.route('/rating')
def rating():
    return render_template("rating.html")








