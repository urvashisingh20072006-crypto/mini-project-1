# ------Student Monthly Budget Analyzer------


name=input("Enter your name:")
monthly_income=float((input("Enter motaly income:")))

food_expenses=float(input("Enter food expenses:"))
travel_expenses=float(input("Enter travel expenses:"))

study_material=float(input("Enter study_material:"))
mobile_internet=float(input("Enter mobile internet recharge:"))

other_expenses=float(input("Enter the other expenses:"))

total_expenses=food_expenses+travel_expenses+study_material+mobile_internet+other_expenses
print("Total Expenses:",total_expenses)


remaining_balance = monthly_income - total_expenses
print("Remaining Balance:",remaining_balance)

saving_rate=(remaining_balance / monthly_income) * 100
print("Saving Rate:",saving_rate)