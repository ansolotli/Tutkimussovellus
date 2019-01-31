from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SiteForm(FlaskForm):
    name = StringField("Site name", [validators.Length(min=2)])

    class Meta:
        csrf = False