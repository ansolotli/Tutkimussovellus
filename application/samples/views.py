from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.samples.models import Sample
from application.samples.forms import SampleForm, UpdateSampleForm
from application.sites.models import Site
from application.auth.models import User

@app.route("/samples", methods=["GET"])
def samples_index():
    return render_template("samples/list.html", samples = Sample.query.all())


@app.route("/samples/new/", methods=["GET"])
def samples_form():
    return render_template("samples/new.html", form = SampleForm(), sites = Site.query.all())


@app.route("/sites/samples/<sample_id>")
def samples_show_one_sample(sample_id):

    s = Sample.query.get(sample_id)

    return render_template("samples/single.html", form = UpdateSampleForm, sample=s)


@app.route("/samples/add", methods=["POST"])
@login_required()
def samples_create():
    form = SampleForm(request.form)

    if not form.validate():
        return render_template("samples/new.html", form = form)

    user = User.query.filter_by(username=current_user.username).first()
    s = Sample(form.samplename.data, form.sampletype.data, form.species.data, form.amount.data)
    
    siteName = request.form.get("sites")
    site = Site.query.filter_by(name=siteName).first()
    s.site_id = site.id

    db.session().add(s)
    
    # lisätään sample tietylle saitille?
    site.samples.append(s)
    user.mysamples.append(s)
    db.session().commit()

    return redirect(url_for("sites_index"))

@app.route("/samples/remove/<sample_id>", methods=["POST"])
@login_required()
def samples_remove(sample_id):

    s = Sample.query.get(sample_id)

    db.session().delete(s)
    db.session().commit()

    return redirect(url_for("sites_index"))