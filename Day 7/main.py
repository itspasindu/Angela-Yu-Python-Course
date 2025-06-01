import random

word_list = ["aardvark", "baboon", "camel"]

choose_word = random.choice(word_list)
print(choose_word)

placeholder = ""
word_length = len(choose_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

display = ""

for letter in choose_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)