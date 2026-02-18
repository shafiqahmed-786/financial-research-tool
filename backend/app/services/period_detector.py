import re

def detect_periods(table):

    header_row = None

    # Find header row containing year-like patterns
    for row in table:
        if not row:
            continue

        joined = " ".join([str(cell) for cell in row if cell])

        if re.search(r"\b20\d{2}\b", joined) or "FY" in joined.upper():
            header_row = row
            break

    if not header_row:
        return []

    periods = []

    for cell in header_row[1:]:
        if not cell:
            continue

        text = str(cell).strip()

        # Detect FY format
        if re.search(r"FY\s?\d+", text.upper()):
            periods.append(text.strip())

        # Detect Year format
        elif re.search(r"\b20\d{2}\b", text):
            periods.append(text.strip())

    return periods
