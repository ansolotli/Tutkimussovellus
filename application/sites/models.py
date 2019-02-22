from application import db
from application.models import Base

from sqlalchemy.sql import text

class Site(Base):

    __tablename__="site"

    name = db.Column(db.String(144), nullable=False, index=True)
    
    samples = db.relationship("Sample", backref="site", lazy=True, cascade="all, delete-orphan", single_parent=True)

    def __init__(self, name):
        self.name = name