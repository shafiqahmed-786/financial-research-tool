import pdfplumber

def extract_tables(filepath):
    tables = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            extracted = page.extract_tables()
            if extracted:
                tables.extend(extracted)
    return tables
