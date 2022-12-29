from datetime import datetime, timedelta
import enum

from app import db


class Priority(enum.Enum):
    low = 1
    medium = 2
    high = 3


class Progress(enum.Enum):
    todo = 1
    doing = 2
    done = 3


def tomorrow_date():
    return datetime.now() + timedelta(days=1)


task_user = db.Table('task_user',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('task_id', db.Integer, db.ForeignKey('task.id'))
                     )


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(2048), nullable=True, default=None)
    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deadline = db.Column(db.DateTime, default=tomorrow_date)
    priority = db.Column(db.Enum(Priority, values_callable=lambda x: [str(member.value) for member in Priority]))
    progress = db.Column(db.Enum(Progress, values_callable=lambda x: [str(member.value) for member in Progress]))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User', secondary=task_user, backref=db.backref('tasks', lazy='dynamic'), lazy='dynamic')
    comments = db.relationship('Comment', backref='tasks', lazy='dynamic')

    def __repr__(self):
        return f"Task('{self.title}', '{self.progress}')"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='category', lazy='dynamic')

    def __repr__(self):
        return f"Category('{self.name}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(2048))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
