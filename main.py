"""
Flask(__name__) establishes resources on the filesystem (aka package).
1. app is control object for flask
2. the Flask initializer uses __name__ param to locate root of webserver
3. static and templates are of folders that are located relative to directory of Flask execution ok"""

from flask import Flask, render_template

from gamereview.Ahmad.app import gamereview_bp1
from gamereview.Max.app import gamereview_bp4
from gamereview.Anthony.app import gamereview_bp3
from gamereview.Andrew.app import gamereview_bp2


app = Flask(__name__)
app.register_blueprint(gamereview_bp1, url_prefix='/Ahmad')
app.register_blueprint(gamereview_bp2, url_prefix='/Andrew')
app.register_blueprint(gamereview_bp3, url_prefix='/Anthony')
app.register_blueprint(gamereview_bp4, url_prefix='/Max')

@app.route('/')
def index():
    return render_template("ahmadhome.html")

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
