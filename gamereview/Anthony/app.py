from flask import Blueprint, render_template

gamereview_bp3 = Blueprint('gamereview3', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp3.route('/')
def index():
    return render_template("anthonyhome.html")
