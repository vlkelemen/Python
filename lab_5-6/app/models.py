from app import db


class ContactInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(13))
    subject = db.Column(db.String(10))
    message = db.Column(db.String(255))
