from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SampleForm(FlaskForm):
    name = StringField("Sample name", [validators.Length(min=2)])
    site_id = StringField("Site", )
    name = StringField("Sample name", [validators.Length(min=2)])
    sampletype = StringField("Sample type", [validators.Length(min=2)])
    species = StringField("Species", [validators.Length(min=2)])
    amount = StringField("Number of Specimen")
    
    class Meta:
        csrf = False