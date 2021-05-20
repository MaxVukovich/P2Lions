from flask import Blueprint, render_template, request
from gamereview.Andrew.foods import Foods
from gamereview.Andrew.bubblesort import bubble

gamereview_bp2 = Blueprint('gamereview2', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp2.route('/')
def index():
    return render_template("andrewhome.html")

# class lab
@gamereview_bp2.route('/andrewminilab', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        k = int(request.form.get("series"))
        return render_template("andrewminilab.html", foodrecs=Foods(k))
    return render_template("andrewminilab.html", foodrecs=Foods(1))

# bubblesort lab
@gamereview_bp2.route('/bubbles1', methods=['GET', 'POST'])
def bubbles():
    if request.form:
        return render_template("bubbles1.html", sort=bubble(request.form.get("var")))
    return render_template("bubbles1.html", sort=bubble("10,9,8,7,6,5,4,3,2,1"))

@gamereview_bp2.route('/forum')
def forum():
    return render_template("forum.html")

@gamereview_bp2.route('/adventuregames')
def adventuregames():
    return render_template("adventuregames.html")