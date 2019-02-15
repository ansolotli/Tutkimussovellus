from application import db
from application.models import Base

class Sample(Base):

    __tablename__="sample"

    samplename = db.Column(db.String(144), nullable=False)
    sampletype = db.Column(db.String(144), nullable=False)
    species = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.String(144), nullable=False)
    
    # site_id = db.Column(db.Integer, db.ForeignKey('site.id'),
    #                        nullable=False)                       

    def __init__(self, samplename, sampletype, species, amount):
        self.samplename = samplename
        self.sampletype = sampletype
        self.species = species
        self.amount = amount