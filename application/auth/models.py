from application import db
from application.models import Base

from sqlalchemy.sql import text

users_sites = db.Table('users_sites',
    db.Column('site_id', db.Integer, db.ForeignKey('site.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('account.id'))
)

users_samples = db.Table("users_samples",
    db.Column('sample_id', db.Integer, db.ForeignKey('sample.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('account.id'))
)

class User(Base):

    __tablename__="account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    mysites = db.relationship("Site", cascade="all, delete-orphan", secondary=users_sites,
        backref=db.backref('mysites', lazy='dynamic'), single_parent=True)

    mysamples = db.relationship("Sample", cascade="all, delete-orphan", secondary=users_samples,
        backref=db.backref('mysites', lazy='dynamic'), single_parent=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return["ADMIN"]

    @staticmethod
    def count_users_sites(userid):
        stmt = text("SELECT COUNT(users_sites.site_id)"
                    " FROM users_sites"
                    " WHERE user_id = :userid").params(userid=userid)

        result = db.engine.execute(stmt)
        return result.fetchone()[0]

    @staticmethod
    def count_users_samples(userid):
        stmt = text("SELECT COUNT(users_samples.sample_id)"
                    " FROM users_samples"
                    " WHERE user_id = :userid").params(userid=userid)

        result = db.engine.execute(stmt)
        return result.fetchone()[0]
    
    @staticmethod
    def list_users_sites(userid):
        stmt = text("SELECT site.id AS siteid, site.name AS sitename"
                    " FROM site"
                    " LEFT JOIN users_sites ON site.id = users_sites.site_id"
                    " WHERE users_sites.user_id = :userid").params(userid=userid)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"siteid":row[0], "sitename":row[1]})
        
        return response
    
    @staticmethod
    def list_users_samples(userid):
        stmt = text("SELECT site.id as siteid, site.name as sitename, sample.samplename as samplename, sample.id as sampleid"
        " FROM users_samples"
        " JOIN sample ON sample.id = users_samples.sample_id"
        " JOIN site ON site.id = sample.site_id"
        " WHERE users_samples.user_id = :userid"
        " ORDER BY site.name").params(userid=userid)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"siteid":row[0], "sitename":row[1], "samplename":row[2], "sampleid":row[3]})

        return response

    @staticmethod
    def count_users_per_site():
        stmt = text("SELECT site.name AS site, COUNT(DISTINCT account.id) AS count"
                    " FROM account"
                    " LEFT JOIN users_samples ON users_samples.user_id = account.id"
                    " LEFT JOIN sample ON sample.id = users_samples.sample_id"
                    " LEFT JOIN site ON site.id = sample.site_id"
                    " GROUP BY site.id"
                    " ORDER BY count DESC, site")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            if row[0] != None:
                response.append({"site":row[0], "count":row[1]})

        return response