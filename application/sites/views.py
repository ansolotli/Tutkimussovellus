from application import app, db
from flask import redirect, render_template, request, url_for
from application.sites.models import Site

@app.route("/sites", methods=["GET"])
def sites_index():
    return render_template("sites/list.html", sites = Site.query.all())

@app.route("/sites/add", methods=["POST"])
def sites_create():
    s = Site(request.form.get("name"))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("sites_index"))

@app.route("/sites/remove/<site_id>", methods=["POST"])
def sites_remove(site_id):

    s = Site.query.get(site_id)

    db.session().delete(s)
    db.session().commit()

    return redirect(url_for("sites_index"))

@app.route("/sites/update", methods=["POST"])
def sites_update():

    newname = request.form.get("newname")
    oldname = request.form.get("oldname")
    site = Site.query.filter_by(name=oldname).first()
    site.name = newname

    db.session.commit()

    return redirect(url_for("sites_index"))