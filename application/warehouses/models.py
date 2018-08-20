from application import db
from application.auth import models
from application.items import models

from sqlalchemy.sql import text

users = db.Table('account_warehouse',
                 db.Column('account_id', db.Integer,
                           db.ForeignKey('account.id'), primary_key=True),
                 db.Column('warehouse_id', db.Integer,
                           db.ForeignKey('warehouse.id'), primary_key=True)
                 )

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    volume = db.Column(db.Integer)

    users = db.relationship('User', secondary=users, lazy='subquery',
                            backref=db.backref('warehouses', lazy=True))
    
    warehouse_items = db.relationship('Warehouse_item', cascade='delete', lazy=True)

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    @staticmethod
    def find_warehouses_with_item(item):
        stmt = text("SELECT DISTINCT warehouse.name "
                    "FROM warehouse, item, warehouse_item "
                    "WHERE item.name LIKE '% :it %' "
                    "AND item_id = warehouse_id AND warehouse_id = warehouse.id").params(it=item)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name": row[0]})

        for row in res:
            print(row[0])

        return response

    @staticmethod
    def count_warehouses():
        stmt = text("SELECT COUNT(warehouse.id) FROM warehouse")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"count": row[0]})

        return response


class Warehouse_item(db.Model):
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'),
                        primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'),
                        primary_key=True)
    amount = db.Column(db.Integer)

    warehouse = db.relationship("Warehouse", lazy=True)
    item = db.relationship("Item", lazy=True)

    def __init__(self, warehouse, item, amount):
        self.warehouse_id = warehouse.id
        self.item_id = item.id
        self.amount = amount

    def __repr__(self):
        return '{} - {} - {}'.format(self.item_id, self.warehouse_id, self.amount)
