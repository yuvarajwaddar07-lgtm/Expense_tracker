#Mini Project – Expense Tracker

#Create a console-based Expense Tracker
#program in Python that allows the user to record daily expenses and view
#summaries like total spending. Use only the concepts learned till Chapter 6
#(loops, conditionals, lists, dictionaries, and basic input/output).

expense = []  # list of expense dictionaries

print("Welcome to Expense tracker! Control your expense here!")

while True:
    print("\n====MENU====")
    print("1. Add Expense")
    print("2. View all expense")
    print("3. View expense by category")
    print("4. View total spending")
    print("5. Exit")

    choose = input("Choose your option (1-5): ")

    if choose == "1":
        date = input("Enter the date of spending: ")
        category = input("Enter which kind of expense it is: ")
        description = input("Enter bought item name: ")
        amount = float(input("Enter your spending(₹): "))

        entry = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expense.append(entry)
        print("\nExpenses added successfully!!")

    elif choose == "2":
        if len(expense) == 0:
            print("\n⚠️ You haven't added any expenses yet!! Please add expenses.")
        else:
            print("\n----All expense----")
            i = 1
            for e in expense:
                print(f"{i}. {e['date']} | {e['category']} | {e['description']} | ₹{e['amount']}")
                i += 1
            print("------------------------")

    elif choose == "3":
        if len(expense) == 0:
            print("\nNo expenses recorded yet.")
        else:
            category = input("Enter category to view expenses: ")
            filtered = [e for e in expense if e["category"].lower() == category.lower()]
            if len(filtered) == 0:
                print(f"\nNo expenses found for category '{category}'.")
            else:
                print(f"\n----Expenses for category: {category}----")
                total_category = 0
                i = 1
                for e in filtered:
                    print(f"{i}. {e['date']} | {e['description']} | ₹{e['amount']}")
                    total_category += e["amount"]
                    i += 1
                print(f"\nTotal spending for category '{category}': ₹{total_category}")
                print("------------------------")

    elif choose == "4":
        if len(expense) == 0:
            print("\nNo expenses recorded yet.")
        else:
            total = 0
            for e in expense:
                total += e["amount"]
            print(f"\nTotal spending = ₹{total}")

    elif choose == "5":
        print("\nExiting Expense Tracker. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please select a valid option (1-5).")
