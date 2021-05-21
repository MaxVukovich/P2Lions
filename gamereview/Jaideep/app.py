from flask import Blueprint, render_template, request
from gamereview.Jaideep.bubble import bubble

gamereview_bp5 = Blueprint('gamereview5', __name__,
                           template_folder='templates',
                           static_folder='static', static_url_path='assets')


@gamereview_bp5.route('/')
def index():
    return render_template("jaideep.html")


@gamereview_bp5.route('/bubble2', methods=['GET', 'POST'])
def bubble():
    if request.form:
        return render_template("bubble2.html", sort=bubble(request.form.get("var")))
    return render_template("bubble2.html", sort=bubble("10,9,8,7,6,5,4,3,2,1"))
