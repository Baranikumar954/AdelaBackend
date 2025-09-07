import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from db import db,mail

from routes.careers_route import applications_bp
from routes.feedbacks_route import feedbacks_bp
from routes.contact_route import contact_bp

load_dotenv()  # Load .env file

app = Flask(__name__)

# Config from .env
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")  # your Gmail
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")  # app password (not Gmail password!)
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")


# Init DB
db.init_app(app)
mail.init_app(app)

# CORS (allow React frontend)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Register routes

app.register_blueprint(applications_bp)
app.register_blueprint(feedbacks_bp) 
app.register_blueprint(contact_bp)

@app.route("/api/")
def ping():
    return jsonify({"message": "pong from Flask"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(host="0.0.0.0", port=5000, debug=True)
