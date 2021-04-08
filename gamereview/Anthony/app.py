from flask import Blueprint, render_template, request
from gamereview.Anthony.sports import Sports

gamereview_bp3 = Blueprint('gamereview3', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp3.route('/')
def index():
    return render_template("anthonyhome.html")

@gamereview_bp3.route('/anthonyminilab', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        k = int(request.form.get("series"))

        return render_template("anthonyminilab.html", sportrecs=Sports(k))
    return render_template("anthonyminilab.html", sportrecs=Sports(1))