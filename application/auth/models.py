from application import db
from application.models import Base


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)
    role = db.relationship("Role")

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

class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name