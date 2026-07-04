def calculate_balance(transactions):

    if not transactions:
            print("No transactions available.")
            return

    income = 0
    expense = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            income += transaction["amount"]
        elif transaction["type"] == "expense":
            expense += transaction["amount"]

    balance = income - expense

    print("========== BALANCE SUMMARY ==========")

    print(f"\tYour total income is : ${income:.2f}")

    print(f"\tYour total expense is: ${expense:.2f}")

    print("-" * 37)

    print(f"\tYour balance is      : ${balance:.2f}")

    print("=" *37)

def monthly_summary(transactions):

    if not transactions:
            print("No transactions available.")
            return

    categories = set()

    income = 0
    expense = 0 

    for transaction in transactions:
        categories.add(transaction["category"])

    for category in categories:

        income = 0
        expense = 0
        
        for transaction in transactions:
            if category == transaction["category"] and transaction["type"] == "income":
                income += transaction["amount"]
            if category == transaction["category"] and transaction["type"] == "expense":
                expense += transaction["amount"]
        print(f"\nCategory: {category}")
        print(f"Income : ${income:.2f}")
        print(f"Expense: ${expense:.2f}")
        print("-" * 30)
    

def search_category(transactions):
    category = input("Search category: ")

    total = 0

    found = False

    expense_total = 0
    income_total = 0
    
    for transaction in transactions:
        if category.lower() == transaction["category"].lower():

            found = True

            print(f"\nType: {transaction['type']}")
            print(f"Amount: ${transaction['amount']:.2f}")
            print(f"Description: {transaction['description']}")
            print("-" * 30)
            
            if transaction["type"] == "expense":
                expense_total += transaction["amount"]
            else:
                income_total += transaction["amount"]

    
    if found and transaction["type"] == "expense":
        print(f"Total money spent on {category}: ${total:.2f}")
    elif found and transaction["type"] == "income":
        print(f"Total money from {category}: ${total:.2f}")
    else:
        print("No transactions found with that category.")