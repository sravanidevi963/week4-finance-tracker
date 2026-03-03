class ExpenseManager:
    def __init__(self, expenses=None):
        self.expenses = expenses if expenses else []

    def add_expense(self, expense):
        self.expenses.append(expense.to_dict())

    def get_all_expenses(self):
        return self.expenses

    def search_by_category(self, category):
        return [e for e in self.expenses if e["category"].lower() == category.lower()]

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            return self.expenses.pop(index)
        else:
            raise IndexError("Invalid index")