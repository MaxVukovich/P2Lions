from flask import Blueprint, render_template
from gamereview.Ahmad.calculator import Games
from flask import request
gamereview_bp1 = Blueprint('gamereview1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp1.route('/')
def index():
    return render_template("ahmadhome.html")

@gamereview_bp1.route('/games', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        a = int(request.form.get("series"))
        gamerecs = Games(a/a)
        return render_template("games.html", gamerecs=Games(a))
    return render_template("games.html", gamerecs=Games(1))

