from flask import Blueprint, render_template, request
from gamereview.Andrew.foods import Foods

gamereview_bp2 = Blueprint('gamereview2', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp2.route('/')
def index():
    return render_template("andrewhome.html")

@gamereview_bp2.route('/andrewminilab', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        a = int(request.form.get("series"))
        foodrecs = Foods(a/a)
        return render_template("andrewminilab.html", foodrecs=Foods(a))
    return render_template("andrewminilab.html", foodrecs=Foods(1))