from db import db

class Feedbacks(db.Model):
    __tablename__ = "feedbacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_content = db.Column(db.Text, nullable=True)

    def __init__(self, name, email, rating, review_content):
        self.name = name
        self.email = email
        self.rating = rating
        self.review_content = review_content
