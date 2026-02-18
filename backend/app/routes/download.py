from flask import Blueprint, send_file, current_app, jsonify
import os

download_bp = Blueprint("download", __name__)

@download_bp.route("/download/<file_id>", methods=["GET"])
def download(file_id):

    file_path = os.path.join(
        current_app.config["OUTPUT_FOLDER"],
        f"{file_id}.xlsx"
    )

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(file_path, as_attachment=True)
