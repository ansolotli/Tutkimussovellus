from application import db

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    sampletype = db.Column(db.String(144), nullable=False)
    site = db.Column(db.String(144), nullable=False)

    def __init__(self, name, sampletype, site):
        self.name = name
        self.sampletype = sampletype
        self.site = site
