from application import db
from application.models import Base

from sqlalchemy.sql import text

class Site(Base):

    __tablename__="site"

    name = db.Column(db.String(144), nullable=False)

    samples = db.relationship("Sample", backref='sites', lazy=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_samples_for_sites():
        stmt = text("SELECT Site.name AS site,"
                    " COUNT(Sample.id) AS samples FROM Site"
                    " LEFT JOIN Sample ON Site.id = Sample.site_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"site":row[0], "samples":row[1]})
    
        return response