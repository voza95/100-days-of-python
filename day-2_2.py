print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

total_bill_amount =  (total_bill * (tip_percent / 100)) + total_bill
user_tip_amount = total_bill_amount / no_of_people
print(f"Each person should pay {round(user_tip_amount, 2)}")