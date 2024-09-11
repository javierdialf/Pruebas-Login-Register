from utils.db import db;

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True);
    full_name = db.Column(db.String(50), nullable=False);
    email_address = db.Column(db.String(65), nullable=False);
    password = db.Column(db.Text, nullable=False)
    

    def __init__(self, full_name, email_address, password):
        self.full_name = full_name;
        self.email_address = email_address;
        self.password = password;