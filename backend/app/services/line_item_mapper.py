def map_line_item(raw_name):

    name = raw_name.lower().strip()

    # ---- Revenue ----
    if "revenue from" in name:
        return "Revenue"

    # ---- Other Income ----
    if "other source" in name or "other income" in name:
        return "Other Income"

    # ---- Total Income ----
    if name == "total":
        return "Total Income"

    # ---- EBITDA ----
    if "ebitda" in name:
        return "EBITDA"

    # ---- Finance Costs ----
    if "total finance costs" in name:
        return "Finance Costs"

    # ---- Depreciation ----
    if name.startswith("depreciation"):
        return "Depreciation"

    # ---- Profit Before Tax ----
    if "profit before tax" in name:
        return "Profit Before Tax"

    # ---- Tax Expense ----
    if "tax expense" in name:
        return "Tax Expense"

    # ---- Profit After Tax ----
    if "profit after tax" in name:
        return "Profit After Tax"

    return None
