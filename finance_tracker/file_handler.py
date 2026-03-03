import json
import os
import shutil
from datetime import datetime

DATA_FILE = "data/expenses.json"
BACKUP_FOLDER = "data/backup/"

def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    create_backup()
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def create_backup():
    if os.path.exists(DATA_FILE):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = BACKUP_FOLDER + f"expenses_backup_{timestamp}.json"
        shutil.copy(DATA_FILE, backup_file)