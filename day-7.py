import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for element in chosen_word:
    if element == guess:
        print("Correct")
    else:
        print(f"Wrong {element}")