from flask import Blueprint, jsonify, current_app
from app.services.income_statement_extractor import extract_income_statement_v3
from app.services.validation import validate_income_statement
from app.services.excel_generator import generate_excel
from app.services.financial_metrics import calculate_margins
from app.services.advanced_metrics import add_cagr
import os

extract_bp = Blueprint("extract", __name__)


@extract_bp.route("/extract/<file_id>", methods=["POST"])
def extract(file_id):

    upload_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        f"{file_id}.pdf"
    )

    if not os.path.exists(upload_path):
        return jsonify({"error": "File not found"}), 404

    # ---- Extraction ----
    income_data = extract_income_statement_v3(upload_path)

    # ---- Validation ----
    warnings = validate_income_statement(income_data)

    # ---- Metrics ----
    metrics = calculate_margins(income_data)
    metrics = add_cagr(metrics, income_data)

    # ---- Metadata (can later auto-detect) ----
    metadata = {
        "currency": "Unknown",
        "unit": "Unknown",
        "statement_type": "Standalone"
    }

    # ---- Excel Output ----
    output_path = os.path.join(
        current_app.config["OUTPUT_FOLDER"],
        f"{file_id}.xlsx"
    )

    generate_excel(income_data, metadata, metrics, output_path)

    return jsonify({
        "metadata": metadata,
        "periods": income_data["periods"],
        "income_statement": income_data["rows"],
        "metrics": metrics,
        "warnings": warnings
    })


@extract_bp.route("/test-extract", methods=["GET"])
def test_extract():

    upload_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        "test.pdf"
    )

    if not os.path.exists(upload_path):
        return jsonify({"error": "test.pdf not found"}), 404

    income_data = extract_income_statement_v3(upload_path)

    warnings = validate_income_statement(income_data)

    metrics = calculate_margins(income_data)
    metrics = add_cagr(metrics, income_data)

    metadata = {
        "currency": "Unknown",
        "unit": "Unknown",
        "statement_type": "Standalone"
    }

    return jsonify({
        "metadata": metadata,
        "periods": income_data["periods"],
        "income_statement": income_data["rows"],
        "metrics": metrics,
        "warnings": warnings
    })
