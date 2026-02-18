import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(os.path.dirname(BASE_DIR), "uploads")
    OUTPUT_FOLDER = os.path.join(os.path.dirname(BASE_DIR), "outputs")
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024  # 20MB
