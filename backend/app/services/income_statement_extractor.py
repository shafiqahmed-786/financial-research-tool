import re
from .line_item_mapper import map_line_item

def extract_income_statement_v3(filepath):

    structured_output = {
        "periods": [],
        "rows": []
    }

    with open(filepath, "rb") as f:
        import pdfplumber
        with pdfplumber.open(f) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

    lines = full_text.split("\n")

    # ---- STEP 1: Detect Header ----
    header_line = None
    for line in lines:
        if "FY" in line and "Particu" in line:
            header_line = line
            break

    if not header_line:
        return structured_output

    # Extract periods using regex
    periods = re.findall(r"FY\s?\d+", header_line)
    structured_output["periods"] = periods

    # ---- STEP 2: Parse Financial Rows ----
    for line in lines:

        # Skip header
        if line == header_line:
            continue

        # Extract numbers (including decimals & commas)
        numbers = re.findall(r"-?\d[\d,]*\.?\d*", line)

        if len(numbers) < len(periods):
            continue

        # Extract line item name
        first_number_index = line.find(numbers[0])
        raw_name = line[:first_number_index].strip()

        mapped_name = map_line_item(raw_name)

        if not mapped_name:
            continue

        row_data = {
            "line_item": mapped_name
        }

        for i, period in enumerate(periods):
            value = numbers[i].replace(",", "")
            try:
                row_data[period] = float(value)
            except:
                row_data[period] = None

        structured_output["rows"].append(row_data)

    return structured_output
