from application import app, db
from flask import redirect, render_template, request, url_for
from application.samples.models import Sample

@app.route("/samples", methods=["GET"])
def samples_index():
    return render_template("samples/list.html", samples = Sample.query.all())

@app.route("/samples/new/")
def samples_form():
    return render_template("samples/new.html")

@app.route("/samples/", methods=["POST"])
def samples_create():
    s = Sample(request.form.get("name"), request.form.get("sampletype"), 
request.form.get("site"))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("samples_index"))
