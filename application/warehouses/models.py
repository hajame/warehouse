from application import db
from application.auth import models

users = db.Table('account_warehouse',
    db.Column('account_id', db.Integer, 
                db.ForeignKey('account.id'), primary_key=True),
    db.Column('warehouse_id', db.Integer, 
                db.ForeignKey('warehouse.id'), primary_key=True)
)

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    volume = db.Column(db.Integer)
    
    users = db.relationship('User', secondary=users, lazy='subquery',
        backref=db.backref('warehouses', lazy=True))

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume