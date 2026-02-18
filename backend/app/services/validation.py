def validate_income_statement(data):

    warnings = []

    revenue = None
    pat = None
    pbt = None

    for row in data["rows"]:
        if row["line_item"] == "Revenue":
            revenue = row
        if row["line_item"] == "Profit After Tax":
            pat = row
        if row["line_item"] == "Profit Before Tax":
            pbt = row

    if revenue and pat:
        for period in data["periods"]:
            if revenue.get(period) is not None and pat.get(period) is not None:
                if pat[period] > revenue[period]:
                    warnings.append(f"PAT greater than Revenue in {period}")

    if pbt and pat:
        for period in data["periods"]:
            if pbt.get(period) and pat.get(period):
                if pat[period] > pbt[period]:
                    warnings.append(f"PAT greater than PBT in {period}")

    return warnings
