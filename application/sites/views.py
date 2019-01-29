from application import app, db
from flask import redirect, render_template, request, url_for
from application.sites.models import Site
from application.sites.forms import SiteForm

@app.route("/sites", methods=["GET"])
def sites_index():
    return render_template("sites/list.html", sites = Site.query.all())


@app.route("/sites/<site_id>")
def sites_show(site_id):

    s = Site.query.get(site_id)

    return render_template("sites/single.html", site=s)


@app.route("/sites/new/")
def sites_form():
    return render_template("sites/new.html", form = SiteForm())


@app.route("/sites/add", methods=["POST"])
def sites_create():
    form = SiteForm(request.form)

    if not form.validate():
        return render_template("sites/new.html", form = form)

    s = Site(form.name.data)

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("sites_index"))


@app.route("/sites/remove/<site_id>", methods=["POST"])
def sites_remove(site_id):

    s = Site.query.get(site_id)

    db.session().delete(s)
    db.session().commit()

    return redirect(url_for("sites_index"))


@app.route("/sites/update/<site_id>", methods=["POST"])
def sites_rename(site_id):

    s = Site.query.get(site_id)
    s.name = request.form.get("newname")
    db.session.commit()

    return redirect(url_for("sites_show", site_id=site_id))

    