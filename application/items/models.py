from application import db
from application.warehouses import models
from sqlalchemy.sql import text

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    volume = db.Column(db.Integer)

    warehouse_items = db.relationship('Warehouse_item', 
                        cascade='delete', lazy=True)

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    @staticmethod
    def count_items():
        stmt = text("SELECT COUNT(item.id) FROM item")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"count": row[0]})

        return response

    def __repr__(self):
        return '{} - {} - {}'.format(self.id, self.name, self.volume)