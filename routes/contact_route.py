from flask import Blueprint, request, jsonify
from flask_mail import Message
import traceback
from db import mail

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/api/contact", methods=["POST"])
def contact():
    try:
        data = request.json
        name = data.get("fullName")
        user_email = data.get("email")  # user's email from the form
        subject = data.get("subject")
        message = data.get("message")

        # Create message for HR
        msg = Message(
            subject=f"Contact Form Submission: {subject}",
            sender=("Adela Website", user_email),  # shows user's email
            recipients=["barani143kumar@gmail.com"],  # HR email
            body=f"""
You received a new message from the website contact form.

Name: {name}
Email: {user_email}

Subject: {subject}

Message:
{message}
            """
        )

        # So HR can directly reply to user’s email
        msg.reply_to = user_email

        mail.send(msg)

        return jsonify({"message": "Message sent successfully!"}), 200
    except Exception as e:
        print("❌ Error while sending email:", str(e))  
        traceback.print_exc()  # shows full error in Flask console
        return jsonify({"error": str(e)}), 500
        
