from flask import Blueprint, request, jsonify, current_app
from app.utils.file_manager import save_file

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_id, path = save_file(file, current_app.config["UPLOAD_FOLDER"])

    return jsonify({
        "file_id": file_id,
        "message": "File uploaded successfully"
    })
