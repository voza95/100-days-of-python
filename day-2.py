first_large_number = 123_456
second_large_number = 987_654.232
result_str = str(first_large_number) + str(second_large_number)
result = first_large_number + second_large_number
print(result)
print(result_str)
print(type(result))

print("##################################")

user_number = input("Enter a two digit number: ")

num_1 = int(user_number[0])
num_2 = int(user_number[1])
# f String
print(f"Sum of two digit number is: {num_1 + num_2}")

print(8 / 3)
print(8 // 3)
print(round(8 / 3, 2))
print(2 ** 3)

age = int(input("What is your age? \n"))

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
moths_remaining = years_remaining * 12

print(f"You have {days_remaining} days remaining, {weeks_remaining} weeks remaining, {moths_remaining} months remaining.")
