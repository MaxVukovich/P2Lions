from flask import Blueprint

gamereview_bp1 = Blueprint('gamereview1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp1.route('/')
def index():
    return "Ahmad is cool"
