import os
import uuid

def generate_file_id():
    return str(uuid.uuid4())

def save_file(file, upload_folder):
    file_id = generate_file_id()
    filename = f"{file_id}.pdf"
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    return file_id, filepath

class FinancialStatement:
    def __init__(self, metadata, data):
        self.metadata = metadata
        self.data = data

    def to_dict(self):
        return {
            "metadata": self.metadata,
            "data": self.data
        }
