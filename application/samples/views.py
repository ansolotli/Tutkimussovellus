from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.samples.models import Sample
from application.samples.forms import SampleForm
from application.sites.models import Site

@app.route("/samples", methods=["GET"])
def samples_index():
    return render_template("samples/list.html", samples = Sample.query.all())

@app.route("/sites/<site_id>", methods=["GET"])
def samples_list(site_id):
    return render_template("sites/single.html", samples = Sample.query.filter(site_id = site_id))



@app.route("/samples/new/", methods=["GET"])
def samples_form():
    return render_template("samples/new.html", form = SampleForm(), sites = Site.query.all())

@app.route("/samples/add", methods=["POST"])
@login_required
def samples_create():
    form = SampleForm(request.form)

    if not form.validate():
        return render_template("samples/new.html", form = form)

    s = Sample(form.name.data, form.sampletype.data, form.species.data, form.amount.data)
    
    siteName = request.form.get("sites")
    site = Site.query.filter_by(name=siteName).first()
    s.site_id = site.id

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("sites_index"))