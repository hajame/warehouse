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

    warehouse_items = db.relationship(
        'Warehouse_item', cascade='delete', lazy=True)

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    # How much of warehouse volume is occupied
    @staticmethod
    def filled_volume(id):
        stmt = text("SELECT SUM(warehouse_item.amount * item.volume) "
                    "FROM warehouse_item, item WHERE warehouse_id = :param "
                    "AND warehouse_item.item_id = item.id;").params(param=id)
        res = db.engine.execute(stmt)
        warehouse_volume = res.fetchone()[0]

        if not warehouse_volume:
            return 0

        return warehouse_volume


    @staticmethod
    def fits(id, amount):

        warehouse_status = Warehouse.filled_volume(id)
        if warehouse_status + amount < 0:
            return False

        stmt = text("SELECT volume from warehouse "
                    "WHERE warehouse.id = :param ;").params(param=id)
        res = db.engine.execute(stmt)
        volume = res.fetchone()[0]

        if warehouse_status + amount > volume:
            return False

        return True


    @staticmethod
    def find_warehouses_with_item(id):
        stmt = text("SELECT DISTINCT warehouse.id, warehouse.name, warehouse_item.amount "
                    "FROM warehouse, item, warehouse_item WHERE item.id = :param "
                    "AND item.id = warehouse_item.item_id "
                    "AND warehouse_item.warehouse_id = warehouse.id "
                    "ORDER BY warehouse_item.amount DESC ;").params(param=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1], "amount": row[2]})

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
