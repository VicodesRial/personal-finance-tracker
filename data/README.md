# Personal Finance Tracker

A command-line Personal Finance Tracker built with Python that allows users to record income and expenses, manage transactions, and generate financial reports. Data is stored persistently using JSON.

---

## Features

Add income
Add expenses
View all transactions
Update existing transactions
Delete transactions
Search transactions by category
View balance summary
View monthly/category summaries
Automatic unique transaction IDs
Persistent storage with JSON

---

## Technologies Used

- Python 3
- JSON
- Pandas

---

## Concepts Practiced

- Functions
- Lists
- Dictionaries
- CRUD Operations
- Modular Programming
- File Handling
- JSON Serialization
- Exception Handling
- Data Processing with Pandas

---

## Project Structure

```
finance_tracker/
│
├── main.py          # Controls the application
├── menu.py          # Menu interface
├── transactions.py  # CRUD operations
├── reports.py       # Financial reports
├── storage.py       # JSON save/load
├── utils.py         # Helper functions
└── transactions.json
```

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

- Add transaction dates
- Export reports to CSV
- Sort transactions
- Budget tracking
- Graphs and charts
- SQLite database support
- GUI version using Tkinter
- Web version using Flask or FastAPI

---

## Author

Vicode 7