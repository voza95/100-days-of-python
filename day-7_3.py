import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

end_of_game = False

empty_list_for_each_letter = ["-" for i in chosen_word]
print(empty_list_for_each_letter)



while(not end_of_game):
    guess = input("Guess a letter: ").lower()
    for (index, element) in enumerate(chosen_word):
        if element == guess:
            empty_list_for_each_letter[index] = element    
    
    print(empty_list_for_each_letter)

    if "-" not in empty_list_for_each_letter:
        end_of_game = True
        print("You have completed the code")