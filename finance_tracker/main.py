from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import load_expenses, save_expenses
from finance_tracker.reports import total_expenses, category_breakdown, monthly_report

def main():
    data = load_expenses()
    manager = ExpenseManager(data)

    while True:
        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Monthly Report")
        print("5. Category Breakdown")
        print("6. Delete Expense")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                date = input("Date (YYYY-MM-DD): ")
                amount = input("Amount: ")
                category = input("Category: ")
                description = input("Description: ")

                expense = Expense(date, amount, category, description)
                manager.add_expense(expense)
                save_expenses(manager.get_all_expenses())
                print("Expense added successfully!")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            expenses = manager.get_all_expenses()
            for i, e in enumerate(expenses):
                print(f"{i}. {e}")

        elif choice == "3":
            category = input("Enter category: ")
            results = manager.search_by_category(category)
            for r in results:
                print(r)

        elif choice == "4":
            month = input("Enter month (YYYY-MM): ")
            report = monthly_report(manager.get_all_expenses(), month)
            for r in report:
                print(r)

        elif choice == "5":
            breakdown = category_breakdown(manager.get_all_expenses())
            for k, v in breakdown.items():
                print(f"{k}: {v}")

        elif choice == "6":
            index = int(input("Enter index to delete: "))
            try:
                manager.delete_expense(index)
                save_expenses(manager.get_all_expenses())
                print("Deleted successfully!")
            except Exception as e:
                print("Error:", e)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()