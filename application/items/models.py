from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    volume = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    def __init__(self, name, volume, amount):
        self.name = name
        self.volume = volume
        self.amount = amount
