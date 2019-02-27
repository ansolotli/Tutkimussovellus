from flask_wtf import FlaskForm
from wtforms import StringField, validators

class AddSampleForm(FlaskForm):
    site_id = StringField("Site")
    samplename = StringField("Sample name", [validators.Length(min=2)])
    sampletype = StringField("Sample type", [validators.Length(min=2)])
    species = StringField("Species", [validators.Length(min=2)])
    amount = StringField("Number of Specimen", [validators.Length(min=1)])
    
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
    sitename = StringField("Site")
    samplename = StringField("Sample name", [validators.Length(min=2, max=20)])
    sampletype = StringField("Sample type", [validators.Length(min=2, max=20)])
    species = StringField("Species", [validators.Length(min=2, max=40)])
    amount = StringField("Number of Specimen", [validators.Length(min=1, max=4)])
    
    class Meta:
        csrf = False