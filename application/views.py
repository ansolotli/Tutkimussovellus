from flask import render_template
from application import app
from application.sites.models import Site

@app.route("/")
def index():
    return render_template("index.html")