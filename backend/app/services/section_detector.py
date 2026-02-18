def is_income_statement_row(row):
    if not row or not row[0]:
        return False

    text = row[0].lower()

    income_keywords = [
        "revenue",
        "income",
        "profit",
        "expense",
        "tax",
        "cost"
    ]

    return any(keyword in text for keyword in income_keywords)
