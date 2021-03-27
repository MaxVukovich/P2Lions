from flask import Blueprint

gamereview_bp4 = Blueprint('gamereview4', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp4.route('/')
def index():
    return "Max is cool"
