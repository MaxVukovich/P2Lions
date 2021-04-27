from flask import Blueprint, render_template
from gamereview.Ahmad.calculator import Games
from flask import request
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'I<+g/P2N$}0GXO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logindatabase.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
# IMPORTANT - GENERATES CSRF TOKEN
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model): #Creates columns inside of the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True) #username column
    email = db.Column(db.String(50), unique=True) #email column
    password = db.Column(db.String(80)) #password column

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
gamereview_bp1 = Blueprint('gamereview1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp1.route('/')
def index():
    return render_template("ahmadhome.html")

@gamereview_bp1.route('/games', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        k = int(request.form.get("series"))
        return render_template("games.html", gamerecs=Games(k))
    return render_template("games.html", gamerecs=Games(1))

@gamereview_bp1.route('/bubblesort')
def bubbles():
    return render_template("bubbles.html")


