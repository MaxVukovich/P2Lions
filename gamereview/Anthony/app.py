from flask import Blueprint, render_template, request
from gamereview.Anthony.sports import Sports
from gamereview.Anthony.bubblesort import bubble

gamereview_bp3 = Blueprint('gamereview3', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp3.route('/')
def index():
    return render_template("anthonyhome.html")

@gamereview_bp3.route('/GameOfTheMonthForm')
def gamemonth():
    return render_template("GameOfTheMonthForm.html")

@gamereview_bp3.route('/anthonyminilab', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        k = int(request.form.get("series"))

        return render_template("anthonyminilab.html", sportrecs=Sports(k))
    return render_template("anthonyminilab.html", sportrecs=Sports(1))

@gamereview_bp3.route('/bubblesort1', methods=['GET', 'POST'])
def bubbles():
    if request.form:
        return render_template("bubblesort1.html", sort=bubble(request.form.get("var")))
    return render_template("bubblesort1.html", sort=bubble("10,9,8,7,6,5,4,3,2,1"))

