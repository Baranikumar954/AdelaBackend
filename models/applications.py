from db import db

class Application(db.Model):
    __tablename__ = "applications"   # explicit table name

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)

    job_position = db.Column(db.String(120), nullable=False)

    cover_letter = db.Column(db.Text, nullable=False)  # for large text

    resume_path = db.Column(db.String(255), nullable=False)  # path to file
