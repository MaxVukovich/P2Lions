from flask import Blueprint, render_template


gamereview_bp1 = Blueprint('gamereview1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp1.route('/')
def index():
    return render_template("ahmadhome.html")
