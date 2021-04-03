from flask import Blueprint, render_template, request
from gamereview.Max.shows import Shows

gamereview_bp4 = Blueprint('gamereview4', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp4.route('/')
def index():
    return render_template("maxhome.html")

@gamereview_bp4.route('/maxminilab', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        a = int(request.form.get("series"))
        showrecs = Shows(a/a)
        return render_template("maxminilab.html", showrecs=Shows(a))
    return render_template("maxminilab.html", showrecs=Shows(1))