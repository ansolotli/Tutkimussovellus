from application import app, db
from flask import redirect, render_template, request, url_for
from application.sites.models import Site

@app.route("/sites", methods=["GET"])
def sites_index():
    return render_template("sites/list.html", sites = Site.query.all())

@app.route("/sites/new/")
def sites_form():
    return render_template("sites/new.html")

@app.route("/sites/", methods=["POST"])
def sites_create():
    s = Site(request.form.get("name"))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("sites_index"))
