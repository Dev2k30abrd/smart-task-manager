from extensions import db


class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text)

    priority = db.Column(db.String(50))

    status = db.Column(db.String(50), default='Pending')

    due_date = db.Column(db.String(50))