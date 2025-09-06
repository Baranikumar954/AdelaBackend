import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from db import db
from routes.careers_route import applications_bp

load_dotenv()  # Load .env file

app = Flask(__name__)

# Config from .env
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init DB
db.init_app(app)

# CORS (allow React frontend)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Register routes
app.register_blueprint(applications_bp)

@app.route("/api/")
def ping():
    return jsonify({"message": "pong from Flask"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(host="0.0.0.0", port=5000, debug=True)
