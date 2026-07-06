# Personal Finance Tracker

A command-line Personal Finance Tracker built with Python that allows users to record income and expenses, manage transactions, and generate financial reports. Data is stored persistently using JSON.

---

## Features

- Add income
- Add expenses
- View all transactions
- Update existing transactions
- Delete transactions
- Search transactions by category
- View balance summary
- View monthly/category summaries
- View transaction statistics
- Sort transactions
- Export transactions to CSV
- Import transactions from CSV
- Automatic transaction dates
- Automatic unique transaction IDs
- Persistent storage with JSON
- Formatted transaction tables using Pandas

---

## Technologies Used

- Python 3
- Pandas
- JSON
- CSV
- Git
- GitHub

## Concepts Practiced

- Functions
- Lists
- Dictionaries
- CRUD Operations
- Modular Programming
- File Handling
- JSON Serialization
- CSV Import/Export
- Exception Handling
- Data Processing with Pandas
- List Comprehensions
- Generator Expressions
- Sorting with `sorted()`
- Lambda Functions

---

## Project Structure

```
finance_tracker/
│
├── data/
│   ├── transactions.json
│   └── output.csv
│
├── main.py
├── menu.py
├── reports.py
├── storage.py
├── transactions.py
├── utils.py
├── README.md
└── requirements.txt
```

---
## Example menu


===== Personal Finance Tracker =====

1. Add Income
2. Add Expense
3. View Transactions
4. Update Transaction
5. Delete Transaction
6. View Balance
7. Search by Category
8. Monthly Summary
9. Export to CSV
10. Import from CSV
11. Sort Transactions
12. Statistics
13. Exit

---
## Example Transaction

```json
{
    "id": 1,
    "type": "expense",
    "amount": 15.75,
    "category": "Food",
    "description": "Chipotle"
}
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Vicode7/CLI-Finance-Tracker.git
```

2. Navigate to the project

```bash
cd personal-finance-tracker
```

3. Install dependencies

```bash
pip install pandas
```

4. Run the application

```bash
python main.py
```

---

## Future Improvements

- Budget tracking
- Search by date range
- SQLite database support
- Charts and graphs
- GUI version with Tkinter
- Web version with Flask or FastAPI

---

## Author

VicodesRial