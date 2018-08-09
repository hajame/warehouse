from application import db

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    volume = db.Column(db.Integer)
   
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
