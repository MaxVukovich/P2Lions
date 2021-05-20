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

app.config['SECRET_KEY'] = 'I<+g/P2N$}0GXOf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))



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

@gamereview_bp1.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return redirect(url_for('login'))

    return render_template('login.html', form=form)

@gamereview_bp1.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@gamereview_bp1.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@gamereview_bp1.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


