def calculate_cagr(start, end, years):
    if start == 0 or start is None:
        return None
    return ((end / start) ** (1 / years) - 1) * 100


def add_cagr(metrics, income_data):

    periods = income_data["periods"]

    if len(periods) < 3:
        return metrics

    first = periods[-1]
    last = periods[0]
    years = len(periods) - 1

    revenue = None
    pat = None

    for row in income_data["rows"]:
        if row["line_item"] == "Revenue":
            revenue = row
        if row["line_item"] == "Profit After Tax":
            pat = row

    if revenue:
        metrics["revenue_cagr"] = {
            "CAGR": calculate_cagr(
                revenue[first],
                revenue[last],
                years
            )
        }

    if pat:
        metrics["pat_cagr"] = {
            "CAGR": calculate_cagr(
                pat[first],
                pat[last],
                years
            )
        }

    return metrics
