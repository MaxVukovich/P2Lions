"""
Flask(__name__) establishes resources on the filesystem (aka package).
1. app is control object for flask
2. the Flask initializer uses __name__ param to locate root of webserver
3. static and templates are of folders that are located relative to directory of Flask execution ok"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import Flask, render_template, redirect, url_for, request, session
from gamereview.Ahmad.app import gamereview_bp1
from gamereview.Max.app import gamereview_bp4
from gamereview.Anthony.app import gamereview_bp3
from gamereview.Andrew.app import gamereview_bp2
from gamereview.Jaideep.app import gamereview_bp5



app = Flask(__name__)
app.register_blueprint(gamereview_bp1, url_prefix='/Ahmad')
app.register_blueprint(gamereview_bp2, url_prefix='/Andrew')
app.register_blueprint(gamereview_bp3, url_prefix='/Anthony')
app.register_blueprint(gamereview_bp4, url_prefix='/Max')
app.register_blueprint(gamereview_bp5, url_prefix='/Jaideep')
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
@app.route('/')
def index():
    return render_template("home.html")
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
