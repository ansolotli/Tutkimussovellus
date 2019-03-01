from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class AddSampleForm(FlaskForm):
    site_id = SelectField("Site", coerce=int)
    
    samplename = StringField("Sample name", [validators.Length(min=2, max=20)])
    sampletype = StringField("Sample type", [validators.Length(min=2, max=20)])
    species = StringField("Species", [validators.Length(min=2, max=40)])
    amount = StringField("Number of Specimen", [validators.Length(min=1, max=4)])
    
    class Meta:
        csrf = False

class ShowSampleForm(FlaskForm):
    samplename = StringField("Sample name", [validators.Length(min=2, max=20)])
    sampletype = StringField("Sample type", [validators.Length(min=2, max=20)])
    species = StringField("Species", [validators.Length(min=2, max=40)])
    amount = StringField("Number of Specimen", [validators.Length(min=1, max=4)])
    
    class Meta:
        csrf = False

class EditSampleForm(FlaskForm):
    site_id = SelectField("Site", coerce=int)

    samplename = StringField("Sample name", [validators.Length(min=2, max=20)])
    sampletype = StringField("Sample type", [validators.Length(min=2, max=20)])
    species = StringField("Species", [validators.Length(min=2, max=40)])
    amount = StringField("Number of Specimen", [validators.Length(min=1, max=4)])
    
    class Meta:
        csrf = False