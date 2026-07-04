import json

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

    