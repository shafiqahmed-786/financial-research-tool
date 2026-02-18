from flask import Flask
from flask_cors import CORS
from .config import Config
from .routes.upload import upload_bp
from .routes.extract import extract_bp
from .routes.download import download_bp
from .utils.logger import setup_logger
from .routes.download import download_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    # Ensure upload/output folders exist
    import os
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)

    setup_logger()

    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(extract_bp, url_prefix="/api")
    app.register_blueprint(download_bp, url_prefix="/api")

    return app
