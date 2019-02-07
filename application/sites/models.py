from application import db
from application.models import Base

class Site(Base):

    __tablename__="site"

    name = db.Column(db.String(144), nullable=False)

    samples = db.relationship("Sample", backref='sites', lazy=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
