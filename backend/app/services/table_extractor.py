import pdfplumber

def extract_all_tables(filepath):
    tables = []
    with pdfplumber.open(filepath) as pdf:
        for page_number, page in enumerate(pdf.pages):
            extracted_tables = page.extract_tables()
            if extracted_tables:
                for table in extracted_tables:
                    tables.append({
                        "page": page_number + 1,
                        "table": table
                    })
    return tables
