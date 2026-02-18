def calculate_growth(current, previous):
    if previous == 0 or previous is None:
        return None
    return ((current - previous) / previous) * 100


def calculate_margins(income_data):

    periods = income_data["periods"]
    rows = income_data["rows"]

    revenue = None
    ebitda = None
    pat = None

    for row in rows:
        if row["line_item"] == "Revenue":
            revenue = row
        elif row["line_item"] == "EBITDA":
            ebitda = row
        elif row["line_item"] == "Profit After Tax":
            pat = row

    metrics = {
        "ebitda_margin": {},
        "pat_margin": {},
        "revenue_growth": {},
        "pat_growth": {}
    }

    # ---- Margins ----
    if revenue:
        for period in periods:
            rev = revenue.get(period)

            if ebitda and rev:
                metrics["ebitda_margin"][period] = (
                    (ebitda.get(period, 0) / rev) * 100
                )

            if pat and rev:
                metrics["pat_margin"][period] = (
                    (pat.get(period, 0) / rev) * 100
                )

    # ---- YoY Growth ----
    for i in range(len(periods) - 1):

        current = periods[i]
        previous = periods[i + 1]

        if revenue:
            growth = calculate_growth(
                revenue.get(current),
                revenue.get(previous)
            )
            metrics["revenue_growth"][current] = growth

        if pat:
            growth = calculate_growth(
                pat.get(current),
                pat.get(previous)
            )
            metrics["pat_growth"][current] = growth

    return metrics
