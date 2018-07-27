from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False)
    volume = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    def __init__(self, name, volume, amount):
        self.name = name
        self.volume = volume
        self.amount = amount
