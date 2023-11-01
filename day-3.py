print("Welcome to the rollercoaster!")
height = int(input("Enter you height in cm: "))
age = int(input("Enter your age: "))

if height > 120:
    if age >= 18:
        print("You can ride the rollercoaster! and you're price is $12.")
    elif age < 18 and age > 12:
        print("You can ride the rollercoaster! and you're price is $7.")
    else:
        print("You can ride the rollercoaster! and you're price is $5.")
else:
    print("Sorry, you can't go to rollercoaster yet!")