import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

life = 3

empty_list_for_each_letter = ["-" for i in chosen_word]
print(empty_list_for_each_letter)

guess = input("Guess a letter: ").lower()

for (index, element) in enumerate(chosen_word):
    if element == guess:
        empty_list_for_each_letter[index] = element    
print(empty_list_for_each_letter)