import pdfplumber

def detect_metadata(filepath):
    metadata = {
        "currency": "Unknown",
        "unit": "Unknown",
        "statement_type": "Unknown"
    }

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lower = text.lower()

            if "₹" in text or "rs." in lower:
                metadata["currency"] = "INR"

            if "in crores" in lower:
                metadata["unit"] = "Crores"
            elif "in lakhs" in lower:
                metadata["unit"] = "Lakhs"
            elif "in millions" in lower:
                metadata["unit"] = "Millions"

            if "consolidated" in lower:
                metadata["statement_type"] = "Consolidated"
            elif "standalone" in lower:
                metadata["statement_type"] = "Standalone"

    return metadata
