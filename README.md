Expense Tracker  

lightweight, terminal-based Expense Tracker application built with Python. This project is modularly designed to help users log, categorize, search, and audit their financial expenses efficiently through a clean Command Line Interface (CLI).


⚙️ Features
-Expense Log Management: Dynamically add, view, and delete recorded expenses.
-Financial Analytics: Calculate immediate totals and view a structured expense summary.
-Targeted Search: Query existing records to isolate specific expenses.
-Error Resilience: Robust runtime input validation handling empty values, out-of-bounds selectors, and ValueError occurrences.Decoupled Architecture: Clean separation of concerns -between core application loop orchestration (main.py) and business logic operations (utils.py).

📂 Folder Structuretextexpense-tracker/
│
├── .venv/                 # Local isolated Python environment (Git ignored)
├── .gitignore             # Standard rules to exclude .venv, caches, and system files
├── README.md              # Project documentation and developer guide
├── main.py                # Application entry point and CLI menu router
├── requirements.txt       # Project dependencies metadata
└── utils.py               # Business logic core layer (add, search, delete, etc.)


Installation 
StepsFollow these steps to set up the development environment locally:
1. # Ensure you are inside the project's root directory

2. # Create the virtual environment 
python -m venv .venv

# Activate the environment (Windows)
.venv\Scripts\activate

# Activate the environment (Mac/Linux)
source .venv/bin/activate

3. # Install DependenciesInstall all packages locked in the project manifest
pip install -r requirements.txt



User Interface Preview:
1. Add Expense
2. Show Expenses
3. Show Total
4. Search Expense
5. Delete Expense
6. Summery expense
7. Exit

Select : 


🔮 Future Improvements

-Persistent Storage Layer: Migrate runtime tracking into a local structured format (such as a SQLite database or a JSON/CSV serialization engine) so records persist after exiting.

-Architectural Refactoring: Refactor the menu-routing layer. Currently, your main.py passes the menu option choice integer ures into every helper method (e.g., utils.add_expense(ures)). The business logic functions in utils.py should be refactored to take functional parameters (like amount, category, or item_name) instead of the selection ID.

-Enhanced Visual Dashboards: Integrate a CLI charting framework like plotext or standard terminal ASCII tables to display the summery_expense module cleanly.

-Comprehensive Test Suite: Implement unit and integration testing workflows using pytest to validate core accounting mechanics.