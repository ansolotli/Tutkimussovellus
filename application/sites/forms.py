from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SiteForm(FlaskForm):
    name = StringField("Site name", [validators.Length(min=2, max=20)])

    class Meta:
        csrf = False

class RenameSiteForm(FlaskForm):
    name = StringField("Site name", [validators.Length(min=2, max=20)])

    class Meta:
       csrf = False 

class SearchSiteForm(FlaskForm):
    name = StringField("name", [validators.Length(max=20)])

    class Meta:
        csrf = False