from flask import Blueprint

gamereview_bp = Blueprint('gamereview', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"
