def total_expenses(expenses):
    return sum(e["amount"] for e in expenses)

def category_breakdown(expenses):
    result = {}
    for e in expenses:
        category = e["category"]
        result[category] = result.get(category, 0) + e["amount"]
    return result

def monthly_report(expenses, month):
    return [e for e in expenses if e["date"].startswith(month)]