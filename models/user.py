from commons import database as db


class User(db.Model):
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(128), unique=True)
    
    def __init__(self, phone_number):
        self.phone_number = phone_number
