import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from models.applications import Application
from db import db

applications_bp = Blueprint("applications_bp", __name__)

# Folder to save resumes
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads", "resumes")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # create folder if not exists

@applications_bp.route("/api/careers", methods=["POST"])
def set_application():
    try:
        # Get form fields
        name = request.form.get("name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        job_position = request.form.get("job_position")
        cover_letter = request.form.get("cover_letter")  # optional but included

        # Get file
        resume_file = request.files.get("resume")
        if not resume_file:
            return jsonify({"error": "Resume file is required"}), 400

        # Secure the filename
        filename = secure_filename(resume_file.filename)

        # Save file to local folder
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        resume_file.save(file_path)

        # Save to DB
        application = Application(
            name=name,
            email=email,
            phone_number=phone_number,
            job_position=job_position,
            cover_letter=cover_letter,
            resume_path=file_path
        )

        db.session.add(application)
        db.session.commit()

        return jsonify({"message": "Application submitted successfully!"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
