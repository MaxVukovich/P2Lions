from flask import Blueprint, render_template

gamereview_bp4 = Blueprint('gamereview4', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp4.route('/')
def index():
    return render_template("maxhome.html")

@gamereview_bp4.route('/maxminilab')
def minilab():
    return render_template("maxminilab.html")

#