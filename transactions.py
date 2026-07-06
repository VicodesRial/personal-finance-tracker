import pandas as pd
from utils import get_current_date

def generate_transaction_id(transactions):

    if not transactions:
        return 1

    if transactions:
        highest_id = max(transaction["id"] for transaction in transactions)
        transaction_id = highest_id + 1
        return transaction_id

def add_income(transactions):
    try:
        amount = float(input("Enter  amount: "))
    except ValueError:
         print("Invalid amount. Please enter a number.")
    category = input("Category: ")
    description = input("Description: ")

    transaction = {
        "id": generate_transaction_id(transactions),
        "type": "income",
        "date": get_time_of_day(),
        "amount": amount,
        "category": category,
        "description": description
    }

    transactions.append(transaction)

    print("Transaction added succesfully!")

def add_expense(transactions):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
         print("Invalid amount. Please enter a number.")
    category = input("Category: ")
    description = input("Description: ")

    transaction = {
        "id": generate_transaction_id(transactions),
        "type": "expense",
        "date": get_time_of_day(),
        "amount": amount,
        "category": category,
        "description": description
    }

    transactions.append(transaction)

    print("Transaction added succesfully!")

def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return

    df = pd.DataFrame(transactions)
    df["id"] = df["id"].apply(lambda x: f"{x:08d}")
    df["amount"] = df["amount"].apply(lambda x: f"${x:.2f}")
    
    df = df.rename(columns=[
        [
            "ID",
            "Date",
            "Type",
            "Category",
            "Amount",
            "Description"
        ]
    ])

    pd.set_option("display.colheader_justify", "left")
    print(df.to_string(index=False))

def update_transactions(transactions):
    try:
        transaction_id = int(input("Enter transaction ID to update: "))
    except ValueError:
        print("Invalid transaction ID.")
        return

    found = False

    for transaction in transactions:
        if transaction["id"] == transaction_id:

            found = True

            print("===== Update =====")
            print("1. Amount ")
            print("2. Category")
            print("3. Description")

            try:
                choice = int(input("Choose an option: "))
                if 1 <= choice <= 3 :
                    if choice == 1:
                        while True:
                            try:
                                amount = float(input("Enter new amount: "))
                                transaction["amount"] = amount
                                break
                            except ValueError:
                                print("Invalid amount. Please enter a number.")
                        
                    elif choice == 2:
                        category = input("Enter new category")
                        transaction["category"] = category
                        
                    elif choice == 3:
                        description = input("Enter new description")
                        transaction["description"] = description
                    
                    print(f"Transaction {transaction_id} updated successfully!")
                    return

                else:
                    print("Please enter a number between 1 and 3.")

            except ValueError:
                print("Invalid input. Please enter a number.")
    if not found:
        print("No transactions found with matching ID")

def delete_transactions(transactions):

    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
    except ValueError:
        print("Invalid transaction ID.")
        return

    found = False

    for transaction in transactions:
        if transaction["id"] == transaction_id:

            print("Transaction found.")
            print(f"ID: {transaction['id']}")
            print("Type: " + transaction['type'])
            print(f"Amount: {transaction['amount']}")
            print("Category: " + transaction['category'])
            print("Description: " + transaction['description'])

            found = True
            print("Delete Transaction? ")
            delete = input("(Y/N): ")
            if delete.lower() == "y":
                transactions.remove(transaction)
                print("Transaction deleted successfully!")
                return
            elif delete.lower() == "n":
                print("Deletion cancelled.")
                return
            else:
                print("Please enter Y or N.")

    if not found:
        print("No transactions found with matching ID")

def sort_transactions(transactions):
    print("===== Sort Transactions =====")
    print("Sort by: ")
    print("1. ID")
    print("2. Date")
    print("3. Amount")
    print("4. Category")
    print("5. Type")
    while True:
        try:
            choice = int(input("Choose a sorting option: "))

            if 1 <= choice <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")
    
    sort_keys = {
        1: "id",
        2: "date",
        3: "amount",
        4: "category",
        5: "type"
    }

    key = sort_keys[choice]
    
    sorted_transactions = sorted(transactions, key=lambda transaction: transaction[key])
    view_transactions(sorted_transactions)
    return sorted_transactions

