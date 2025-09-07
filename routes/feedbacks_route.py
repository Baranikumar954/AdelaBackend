from flask import Blueprint, request, jsonify
from models.feedbacks import Feedbacks
from db import db
from sqlalchemy import func

feedbacks_bp = Blueprint("feedbacks_bp", __name__)

# GET → return avg rating + total reviews
@feedbacks_bp.route("/api/feedbacks/getAvg", methods=["GET"])
def get_feedback_stats():
    avg_rating = db.session.query(func.avg(Feedbacks.rating)).scalar() or 0
    total_reviews = db.session.query(func.count(Feedbacks.id)).scalar() or 0

    return jsonify({
        "average_rating": round(float(avg_rating), 2),
        "total_reviews": total_reviews
    }), 200


# POST → add new feedback
@feedbacks_bp.route("/api/feedbacks", methods=["POST"])
def add_feedback():
    data = request.get_json()

    try:
        new_feedback = Feedbacks(
            name=data.get("name"),
            email=data.get("email"),
            rating=int(data.get("rating")),
            review_content=data.get("reviewContent")
        )
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
