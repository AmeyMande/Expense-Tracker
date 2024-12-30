import calendar
import datetime

class Expense:
    def __init__(self,name,amount,category):
        self.name = name
        self.amount = amount
        self.category = category


    def __repr__(self):
        return f"Expense :{self.name} {self.category} {self.amount:.2f}"
        
def main():
    print("Amey")
    expense_file_path = "expense.csv"
    budget = 30000

    expense = how_much_is_the_expense()

    save_it_in_file(expense , expense_file_path)

    summarize_expenses(expense_file_path,budget)

def how_much_is_the_expense():
    print("how much did you spend")
    expense_name = input("Where did you spend it? : ")
    expense_amount = float(input("How much money have you spent here? : "))
    print(f"Expense name is {expense_name}, {expense_amount}")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]

    while True:
        print("In which category are you spending? : ")
        for i , category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter the category : {value_range} :"))-1

        if selected_index in range(len(expense_categories)):
            selected_category=expense_categories[selected_index]
            print(selected_category)

            new_expense = Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category")
        break

def save_it_in_file(expense :Expense, expense_file_path):

    print(f"Expenses have to be saved in file : {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, budget):
    print("summary of user expenses:")
    expenses =[]
    with open(expense_file_path,'r') as f:
        lines = f.readlines()
        for line in lines:
            #print(line)
            expense_name , expense_amount , expense_category =line.strip().split(",")
            print(f"{expense_name} {expense_amount} {expense_category}")
            line_expense=Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            #print(line_expense)
            expenses.append(line_expense)
            #print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key=expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    #print(amount_by_category)
    print("This is your category wise expenses")
    for key ,amount in amount_by_category.items():
        print(f"{key} : {amount}")

    total_spent = sum([x.amount for x in expenses ])
    print(f"You have spent this much : {total_spent:.2f}")

    remaining_budget = budget - (total_spent)
    print(f"remaining budget : {remaining_budget:.2f}")

    now=datetime.datetime.now()
    days_in_month=calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month - now.day
    print("Remaining days left in this month : ",remaining_days)

    daily_budget = remaining_budget/remaining_days
    print("daily budget : ",daily_budget)

if __name__ == "__main__":
    main()