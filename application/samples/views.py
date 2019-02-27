from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy import text

from application import app, db, login_required
from application.samples.models import Sample
from application.samples.forms import AddSampleForm, ShowSampleForm, EditSampleForm
from application.sites.models import Site
from application.auth.models import User


@app.route("/samples", methods=["GET"])
def samples_index():
    return render_template("samples/list.html", samples = Sample.query.all())


@app.route("/samples/new/<site_id>", methods=["GET"])
def samples_form(site_id):

    form = AddSampleForm()

    form.site_id.choices = [(g.id, g.name) for g in Site.query.order_by(Site.name).all()]
    form.site_id.data=site_id
    
    return render_template("samples/new.html", form = form)


@app.route("/sites/samples/<sample_id>")
def samples_show_one_sample(sample_id):

    sample = Sample.query.get(sample_id)
    site = Site.query.get(sample.site_id)

    return render_template("samples/single.html", form = ShowSampleForm, sample=sample, site = site)


@app.route("/samples/add", methods=["POST"])
@login_required()
def samples_create():

    form = AddSampleForm(request.form)

    # if not form.validate():
    #     form.site_id.choices = [(g.id, g.name) for g in Site.query.order_by(Site.name).all()]
    #     form.site_id.data=site_id
    #     return render_template("samples/new.html", form = form)

    user = User.query.filter_by(username=current_user.username).first()
    s = Sample(form.samplename.data, form.sampletype.data, form.species.data, form.amount.data)
    
    siteid = form.site_id.data
    site = Site.query.get(siteid)
    s.site_id = site.id

    db.session().add(s)
    user.mysamples.append(s)
    db.session().commit()

    return redirect(url_for("samples_show_one_sample", sample_id = s.id))


@app.route("/samples/remove/<sample_id>", methods=["POST"])
@login_required()
def samples_remove(sample_id):

    s = Sample.query.get(sample_id)

    db.session().delete(s)
    db.session().commit()

    return redirect(url_for("sites_index"))


@app.route("/samples/update/<sample_id>", methods=["GET", "POST"])
@login_required()
def samples_update(sample_id):

    sample = Sample.query.get(sample_id)


    form = EditSampleForm(obj=sample)
    form.site_id.choices = [(g.id, g.name) for g in Site.query.order_by(Site.name).all()]


    return render_template("samples/edit.html", sample = sample, form=form)


@app.route("/samples/save/<sample_id>", methods=["GET", "POST"])
@login_required()
def samples_save(sample_id):

    form = EditSampleForm(request.form)

    s = Sample.query.filter_by(id=sample_id).first()
    
    # if not form.validate():
        # form = EditSampleForm(obj=s)
        # form.site_id.choices = [(g.id, g.name) for g in Site.query.order_by(Site.name).all()]
        # return render_template("samples/edit.html", sample=s, form=form)

    siteid = form.site_id.data
    site = Site.query.get(siteid)
    s.site_id = site.id

    s.samplename = form.samplename.data
    s.sampletype = form.sampletype.data
    s.species = form.species.data
    s.amount = form.amount.data

    db.session.commit()

    return redirect(url_for("samples_show_one_sample", sample_id=sample_id)) 