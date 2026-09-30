# Student Expense Tracker

A command-line Python application designed for students to track expenses, manage budgets, and analyze spending patterns across key categories.

## Features

- **Add Expenses:** Log amounts spent into specific categories:
  - Food and Groceries
  - Books and Stationeries
  - Rent and Utilities
  - Transport
  - Entertainment
  - Other
- **Timeframe Summaries:** View text-based breakdown and percentage analytics for:
  - This Week (Last 7 Days)
  - This Month (Last 30 Days)
  - All-Time Summary
- **Budget Alerts:** Set a custom overall budget limit with automatic real-time warnings if spending exceeds the cap.

## Project Structure

The project consists of a single executable script containing:
- `printMenu()`: Displays the user interface choices.
- `get_filtered_expenses()`: Filters transactions using `datetime` and `timedelta` objects based on timeframe settings.
- `main()`: Runs the application runtime loop, handles input validation, and stores runtime data.

## Getting Started

### Prerequisites
- Python 3.x
   No external libraries or pip installations required!

### Running the App
1. Save the code into a file named `expense_tracker.py`.
2. Open your terminal or command prompt.
3. Run the script using the following command:
   bash
   python ExpenseTracker.py
   
   
## 📊 Sample Output Demo
```text
--- Expense Distribution Summary ---
Total Expenditure: 1250.00

Category                  | Amount     | Percentage
--------------------------------------------------
Food & Groceries          | 450.00     |    36.00%
Books & Stationeries      | 150.00     |    12.00%
Rent & Utilities          | 500.00     |    40.00%
Transport                 | 50.00      |     4.00%
Entertainment & Social    | 100.00     |     8.00%
Other                     | 0.00       |     0.00%
--------------------------------------------------
   

