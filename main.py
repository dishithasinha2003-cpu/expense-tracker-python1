prinE = "expenses.csv"


def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter t("Welcome to Expense Tracker")
import csv
from datetime import datetime

FILE_NAMcategory (Food/Travel/Shopping/Others): ")
    description = input("Enter description: ")

    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\nDate\t\tCategory\tAmount\tDescription")
            print("-" * 50)

            for row in reader:
                print("\t".join(row))

    except FileNotFoundError:
        print("No expenses found.\n")


def total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[2])

        print("Total Expense: ₹", total, "\n")

    except FileNotFoundError:
        print("No expenses found.\n")


def main():

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice\n")


main()