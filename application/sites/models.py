from application import db
from application.models import Base

from sqlalchemy.sql import text

class Site(Base):

    __tablename__="site"

    name = db.Column(db.String(144), nullable=False, index=True)
    
    samples = db.relationship("Sample", backref="site", lazy=True, cascade="all, delete-orphan", single_parent=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def samples_per_site():
        stmt = text("SELECT site.name AS name, COUNT(sample.id) AS count FROM sample "
                    "LEFT JOIN site ON site.id = sample.site_id GROUP BY name")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1]})
        
        return response
    
    @staticmethod
    def samples_per_site_and_type():
        stmt = text("SELECT site.name AS name, sample.sampletype AS type, COUNT(sample.id) AS count FROM "
                    "sample LEFT JOIN site ON site.id = sample.site_id GROUP BY name, type")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "type":row[1], "count":row[2]})

        return response

    @staticmethod
    def group_by_species_and_site():
        stmt = text("SELECT site.name AS name, sample.species AS species, COUNT(sample.id) AS count FROM "
                    "sample LEFT JOIN site ON site.id = sample.site_id GROUP BY name, species")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "species":row[1], "count":row[2]})

        return response