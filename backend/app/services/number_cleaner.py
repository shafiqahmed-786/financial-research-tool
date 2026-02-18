def clean_number(value):
    if not value:
        return None

    value = str(value).strip()
    value = value.replace(",", "")

    if value.startswith("(") and value.endswith(")"):
        return -float(value[1:-1])

    try:
        return float(value)
    except:
        return None
