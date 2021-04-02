from flask import Blueprint, render_template
from gamereview.Ahmad.calculator import Games
from flask import request
gamereview_bp1 = Blueprint('gamereview1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp1.route('/')
def index():
    return render_template("ahmadhome.html")

@gamereview_bp1.route('/select-game', methods=['GET', 'POST'])
def search():
    #genres = 'nothing'
    #if request.method == 'POST':
    #genres = request.form.getlist('genre')
    #print(genres)
    #if 'Romance' and 'SciFi' and 'Nonfiction' and 'Comedy' in genres:
    #    return render_template("allgenres.html")
    #if 'Comedy' in genres:
    #    return render_template("index.html")
    #if 'Nonfiction' in genres:
    #    return render_template("index.html")
    #if 'Romance' in genres:
    #    return render_template("index.html")
    #if 'SciFi' in genres:
    #    return render_template("index.html")
    if request.method == 'POST':
        a = int(request.form.get("series"))
        gamerecs = Games(a/a)
        return render_template("select-game.html", gamerecs=Games(a))
    return render_template("select-game.html", gamerecs=Games(1))

