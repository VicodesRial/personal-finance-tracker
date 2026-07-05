def show_menu():
    print("===== Personal Finance Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Update Transaction")
    print("5. Delete Transaction")
    print("6. View Balance")
    print("7. Search by Category")
    print("8. Monthly Summary")
    print("9. Export to csv")
    print("10. Import csv")
    print("11. Exit")



    try:
        choice = int(input("Choose an option: "))
        if 1 <= choice <= 11 :
            return choice
        else:
            print("Please enter a number between 1 and 11.")

    except ValueError:
        print("Invalid input. Please enter a number.")