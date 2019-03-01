from application import db
from application.models import Base

from sqlalchemy.sql import text

class Sample(Base):

    __tablename__="sample"

    samplename = db.Column(db.String(144), nullable=False)
    sampletype = db.Column(db.String(144), nullable=False, index=True)
    species = db.Column(db.String(144), nullable=False, index=True)
    amount = db.Column(db.String(144), nullable=False)
    
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'),
                           nullable=False)                       

    def __init__(self, samplename, sampletype, species, amount):
        self.samplename = samplename
        self.sampletype = sampletype
        self.species = species
        self.amount = amount

    @staticmethod
    def group_by_species():
        stmt = text("SELECT sample.species AS species, COUNT(sample.id) AS count"
                    " FROM sample"
                    " GROUP BY species"
                    " ORDER BY count DESC, species")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"species":row[0], "count":row[1]})

        return response
    
    @staticmethod
    def group_by_type():
        stmt = text("SELECT sample.sampletype AS type, COUNT(sample.id) AS count"
                    " FROM sample"
                    " GROUP BY type"
                    " ORDER BY count DESC, type")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"type":row[0], "count":row[1]})

        return response