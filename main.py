from datetime import datetime, timedelta

def printMenu(): 
    print("\n-------------------------")
    print("  STUDENT EXPENSE TRACKER ")
    print("--------------------------")
    print("1) Add an Expense")
    print("2) View Summary & Analytics")
    print("3) Set/Change Budget Limit")
    print("4) Exit")
    print("-------------------------")

def get_filtered_expenses(transactions, days_back=None):
    """Filters transactions by a timeframe and returns a dictionary of category totals."""
    cat_totals = {c: 0.0 for c in ["Food and Groceries", "Books and Stationeries", "Rent and Utilities", "Transport", "Entertainment", "Other"]}
    if not days_back:
        for t in transactions:
            cat_totals[t["category"]] += t["amount"]
        return cat_totals
    cutoff_date = datetime.now() - timedelta(days=days_back)
    for t in transactions:
        if t["date"] >= cutoff_date:
            cat_totals[t["category"]] += t["amount"]
            
    return cat_totals

def main():
    cat_list = [ "Food and Groceries", "Books and Stationeries", "Rent and Utilities", "Transport", "Entertainment", "Other"]
    transactions = [] 
    budget_limit = 0.0
    while True:
        printMenu()
        if budget_limit > 0:
            all_time_totals = get_filtered_expenses(transactions)
            current_total = sum(all_time_totals.values())
            print(f"Current Budget Limit: ₹{budget_limit:.2f} | Total Spent: ₹{current_total:.2f}")
            if current_total > budget_limit:
                print("WARNING: You have exceeded your budget!")
            print("-------------------------")

        user_input = input("Choose an option (1-4): ").strip()
        if user_input == "1":
            print("\nAvailable Categories:")
            for i, cat in enumerate(cat_list):
                print(f" {i+1}. {cat}")
            
            try:
                cat_idx = int(input("Select category number: ")) - 1
                if cat_idx < 0 or cat_idx >= len(cat_list):
                    print("That category number doesn't exist.")
                    continue
                chosen_cat = cat_list[cat_idx]
            except ValueError:
                print("Please enter a valid integer number.")
                continue

            try:
                amt = float(input(f"Enter amount spent on {chosen_cat}: "))
                if amt < 0:
                    print("Amount cannot be negative.")
                    continue
            except ValueError:
                print("Invalid amount entered.")
                continue
            transactions.append({
                "category": chosen_cat,
                "amount": amt,
                "date": datetime.now()
            })
            print(f"Successfully added ₹{amt:.2f} to {chosen_cat}!")
            if budget_limit > 0:
                new_total = sum(t["amount"] for t in transactions)
                if new_total > budget_limit:
                    print(f"Alert! This expense pushes you over budget by ₹{(new_total - budget_limit):.2f}!")
        elif user_input == "2":
            print("\n--- Choose a Timeframe Summary ---")
            print("1) This Week (Last 7 Days)")
            print("2) This Month (Last 30 Days)")
            print("3) All-Time Summary")
            
            sub_choice = input("Select an option (1-3): ").strip()
            
            if sub_choice == "1":
                days, label = 7, "Weekly (Last 7 Days)"
            elif sub_choice == "2":
                days, label = 30, "Monthly (Last 30 Days)"
            elif sub_choice == "3":
                days, label = None, "All-Time"
            else:
                print("Invalid choice.")
                continue
                
            period_expenses = get_filtered_expenses(transactions, days)
            period_total = sum(period_expenses.values())
            
            print(f"\n--- {label} Summary ---")
            if period_total <= 0:
                print("No expenses found for this time period.")
                continue
                
            print(f"Total Spent in Period: ₹{period_total:.2f}\n")
            print(f"{'Category':<25} | {'Amount':<10} | {'Percentage':<10}")
            print("-" * 52)   
            for k,val in period_expenses.items():
                pct=(val/period_total)*100 
                print(f"{k:<25} | ₹{val:<9.2f} | {pct:>8.1f}%")
                print("-" * 52)
        elif user_input == "3":
            try:
                limit_input = float(input("\nEnter your overall budget limit (0 to disable): "))
                if limit_input < 0:
                    print("Budget limit cannot be negative.")
                    continue
                budget_limit = limit_input
                print(f"Budget limit successfully updated to ₹{budget_limit:.2f}!")
            except ValueError:
                print("Invalid budget amount entered.")
        elif user_input == "4":
            print("\nExiting program... Goodbye!")
            break
        else:
            print("That's not a valid menu choice. Try again.") 
main()