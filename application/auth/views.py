from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from sqlalchemy import text

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = NewUserForm())


@app.route("/auth/add", methods=["POST"])
def auth_create():
    form = NewUserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))


@app.route("/auth/own", methods=["GET"])
@login_required()
def auth_account():

    user = User.query.filter_by(username=current_user.username).first()

    stmt = text(
        "SELECT site.id as siteid, site.name as sitename, sample.samplename as samplename, sample.id as sampleid "
        "FROM users_samples JOIN sample ON sample.id = users_samples.sample_id "
        "JOIN site ON site.id = sample.site_id "
        "WHERE users_samples.user_id = :user_id "
        "ORDER BY site.name"
        ).params(user_id=current_user.id)

    siteslist = db.engine.execute(stmt)

    users_sites = current_user.count_users_sites(current_user.id)
    users_samples = current_user.count_users_samples(current_user.id)

    return render_template("auth/ownaccount.html", user=current_user, sites=siteslist, 
        users_sites=users_sites, users_samples=users_samples)