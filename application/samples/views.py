from flask import redirect, render_template, request, url_for

from application import app, db
from application.samples.models import Sample
from application.samples.forms import SampleForm
from application.sites.models import Site

@app.route("/samples", methods=["GET"])
def samples_index():
    return render_template("samples/list.html", samples = Sample.query.all())

@app.route("/samples/new/")
def samples_form():
    return render_template("samples/new.html", form = SampleForm())

@app.route("/samples/add", methods=["POST"])
def samples_create():
    form = SampleForm(request.form)

    if not form.validate():
        return render_template("samples/new.html", form = form)

    s = Sample(form.name.data, form.sampletype.data, form.species.data, form.amount.data)

    # site = db.session.query(Site).query.filter_by(name=form.name.data).first()
    

    site = Site.query.filter_by(name=form.site_id.data).first()
    s.site_id = site.id

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("sites_index"))