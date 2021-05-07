from flask import Blueprint, render_template, request
from gamereview.Max.shows import Shows

gamereview_bp5 = Blueprint('gamereview5', __name__,
                           template_folder='templates',
                           static_folder='static', static_url_path='assets')


@gamereview_bp5.route('/')
def index():
    return render_template("jaideep.html")

