"""
Flask(__name__) establishes resources on the filesystem (aka package).
1. app is control object for flask
2. the Flask initializer uses __name__ param to locate root of webserver
3. static and templates are of folders that are located relative to directory of Flask execution
"""

from flask import Flask
from gamereview.Ahmad.app import gamereview_bp
from gamereview.Max.app import gamereview_bp
from gamereview.Anthony.app import gamereview_bp
from gamereview.Andrew.app import gamereview_bp


app = Flask(__name__)
app.register_blueprint(gamereview_bp, url_prefix='/Ahmad')
app.register_blueprint(gamereview_bp, url_prefix='/Andrew')
app.register_blueprint(gamereview_bp, url_prefix='/Anthony')
app.register_blueprint(gamereview_bp, url_prefix='/Max')

@app.route('/')
def index():
    return "Student Home Site"


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
