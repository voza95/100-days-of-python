height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height**2))

if bmi < 18.5:
    print(f"You are underweight with {bmi} BMI")
elif bmi < 25:
    print(f"You are normal weight with {bmi} BMI")
elif bmi < 30:
    print(f"You are overweight weight with {bmi} BMI")
elif bmi < 35:
    print(f"You are obese weight with {bmi} BMI")
else:
    print(f"You are clinically obese with {bmi} BMI")