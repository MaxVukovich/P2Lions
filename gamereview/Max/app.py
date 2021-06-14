from flask import Blueprint, render_template, request
from gamereview.Max.shows import Shows
from gamereview.Max.bubblesort import bubbleSort

gamereview_bp4 = Blueprint('gamereview4', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp4.route('/')
def index():
    return render_template("maxhome.html")

@gamereview_bp4.route('/maxrating')
def rating():
    return render_template("maxrating.html")

@gamereview_bp4.route('/maxindividual')
def individual():
    return render_template("maxindividual.html")

@gamereview_bp4.route('/maxminilab', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        k = int(request.form.get("series"))
        return render_template("maxminilab.html", showrecs=Shows(k))
    return render_template("maxminilab.html", showrecs=Shows(1))

@gamereview_bp4.route('/bubblesort', methods=['GET', 'POST'])
def bubblesort():
    if request.form:
        return render_template("bubblesort.html", sort=bubbleSort(request.form.get("var")))
    return render_template("bubblesort.html", sort=bubbleSort("10,9,8,7,6,5,4,3,2,1"))
