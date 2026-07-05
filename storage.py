import json
import pandas as pd
import os

def save_transactions(transactions):

    with open("transactions.json", "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent =4)
    
    print("Transactions saved")

def load_transactions():
    try:
        with open("transactions.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def export_to_csv(transactions):
    directory = "FINANCE_TRACKER/data"
    file_name = "output.csv"

    os.makedirs(directory, exist_ok=True)

    full_path = os.path.join(directory, file_name)

    if not transactions:
        print("No transactions to export")
        return
    else:
        df = pd.DataFrame(transactions)
        df.to_csv(full_path, index=False, encoding='utf-8')
        print(f"Transactions exported successfully to {full_path}")

def import_csv():
    directory = "FINANCE_TRACKER/data"
    file_name = "output.csv"

    os.makedirs(directory, exist_ok=True)

    full_path = os.path.join(directory, file_name)
    if not os.path.exists(full_path):
        print("Nothing to import")
        return
    
    df = pd.read_csv(full_path)
    transactions = df.to_dict(orient="records")
    save_transactions(transactions)
    print("File imported succesfully")

    return transactions