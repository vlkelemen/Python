from . import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=False, nullable=True)
    email = db.Column(db.String(40), unique=False, nullable=True)
    phone = db.Column(db.String(15), unique=False, nullable=True)
    library = db.Column(db.String(15), unique=False, nullable=True)
    message = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f"Name : {self.name}, Email: {self.email}"
