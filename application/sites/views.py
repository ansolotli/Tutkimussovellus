from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy import text

from application import app, db, login_manager, login_required
from application.sites.models import Site
from application.sites.forms import SiteForm, RenameSiteForm, SearchSiteForm
from application.samples.models import Sample
from application.auth.models import User


@app.route("/sites", methods=["GET"])
def sites_index():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    sites = Site.query.order_by(Site.name).paginate(page, per_page, error_out = False)

    next_url = url_for('sites_index', page=sites.next_num) \
        if sites.has_next else None
    prev_url = url_for('sites_index', page=sites.prev_num) \
        if sites.has_prev else None

    return render_template("sites/list.html", sites = sites.items,
                          next_url=next_url, prev_url=prev_url, page = page)

    
@app.route("/sites/<site_id>", methods=["GET"])
def sites_show_one_site(site_id):

    site = Site.query.get(site_id)
    samples = site.samples
    
    return render_template("sites/single.html", site=site, form=RenameSiteForm(), samples=samples)


@app.route("/sites/new/", methods=["GET"])
@login_required()
def sites_form():
    return render_template("sites/new.html", form = SiteForm())


@app.route("/sites/add", methods=["POST"])
@login_required()
def sites_create():
    form = SiteForm(request.form)

    if not form.validate():
        return render_template("sites/new.html", form = form)

    s = Site(form.name.data)

    user = User.query.filter_by(username=current_user.username).first()
    user.mysites.append(s)

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("sites_index"))


@app.route("/sites/remove/<site_id>", methods=["POST"])
@login_required()
def sites_remove(site_id):

    s = Site.query.filter_by(id=site_id).first()

    # user = User.query.filter_by(username=current_user.username).first()
    # s.user_id = user.mysites.query.filter_by(site_id=site_id)

    # if s.user_id != current_user.id:
    #     # tee jotain, esim. 
    #     return login_manager.unauthorized()

    db.session().delete(s)
    db.session().commit()

    return redirect(url_for("sites_index"))


@app.route("/sites/update/<site_id>", methods=["POST"])
@login_required()
def sites_rename(site_id):
    form = RenameSiteForm(request.form)

    s = Site.query.filter_by(id=site_id).first()

    if not form.validate():
        return render_template("sites/single.html", site=s, form=form)

    s.name = form.name.data
    db.session.commit()

    return redirect(url_for("sites_show_one_site", site_id=site_id)) 


@app.route("/sites/search", methods=["GET"])
def sites_search():
    return render_template("sites/search.html", form = SearchSiteForm())


@app.route("/sites/search/results", methods=["GET", "POST"])
def sites_search_results():
    form = SearchSiteForm(request.form)

    if not form.validate():
        return render_template("sites/search.html", form=form, searched=False)

    name = form.name.data

    results = Site.query.filter(Site.name.ilike("%" + name + "%")).order_by(Site.name).all()

    return render_template("sites/search.html", sites = results, form = form, searched=True)


@app.route("/sites/statistics", methods=["GET"])
def see_statistics():

    users_per_site = User.count_users_per_site()

    samples_per_site_and_type = Site.samples_per_site_and_type()
    samples_per_site = Site.samples_per_site()
    group_by_species_and_site = Site.group_by_species_and_site()

    group_by_species = Sample.group_by_species()
    group_by_type = Sample.group_by_type()

    return render_template("sites/stats.html", users_per_site = users_per_site, samples_per_site_and_type = samples_per_site_and_type, samples_per_site = samples_per_site,
    group_by_species = group_by_species, group_by_species_and_site = group_by_species_and_site, group_by_type = group_by_type)