import os
import uuid

def generate_file_id():
    return str(uuid.uuid4())

def save_file(file, upload_folder):
    os.makedirs(upload_folder, exist_ok=True)

    file_id = generate_file_id()
    filename = f"{file_id}.pdf"
    filepath = os.path.join(upload_folder, filename)

    file.save(filepath)

    return file_id, filepath
