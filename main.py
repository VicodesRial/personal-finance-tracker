from menu import show_menu
from transactions import add_expense, add_income, view_transactions, update_transactions, delete_transactions
from reports import calculate_balance, monthly_summary, search_category
from utils import clear_console, pause
from storage import load_transactions, save_transactions

transactions = load_transactions()

while True:
    clear_console()

    choice = show_menu()

    if choice == 1:
        add_income(transactions)
        save_transactions(transactions)
        pause()
    elif choice ==2:
        add_expense(transactions)
        save_transactions(transactions)
        pause()
    elif choice ==3:
        view_transactions(transactions)
        pause()
    elif choice ==4:
        update_transactions(transactions)
        save_transactions(transactions)
        pause()
    elif choice ==5:
        delete_transactions(transactions)
        save_transactions(transactions)
        pause()
    elif choice ==6:
        calculate_balance(transactions)
        pause()
    elif choice == 7:
        search_category(transactions)
        pause()
    elif choice == 8:
        monthly_summary(transactions)
        pause()
    elif choice ==9:
        print("")
        print("====================================")
        print("")
        print("Goodbye!")
        break

