import random
import string
# Christian Rivera
word_bank = ["graves", "talon", "nasus", "darius", "diana", "garen", "taric", "yasuo", "jhin", "ziggs"]
word = random.choice(word_bank)
guesses_left = 11
letters_guessed = []
response = ""
right_answer = (list(word))
alphabet = list(string.ascii_lowercase)

while guesses_left != 0:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    guesses_left -= 1
    join = " ".join(output)
    print(join)
    print("You have %s guesses" % guesses_left)
    if (output) == True:
        print("You won!")
        quit()  # Bad coding
    print("Guessable letters : %s" % alphabet)
    response = input("Name a letter")
    make_guess_lowercase = response.lower()
    letters_guessed.append(make_guess_lowercase)
    if make_guess_lowercase in alphabet:
        alphabet.remove(make_guess_lowercase)
    if guesses_left == 0:
        print("You Lose The Word Was %s" % word)
"""
Outline of Hangman
1. Make a word bank - 10 items
2.select a random item from the list - going to be the word you're going to guess
3.Add user input to a list of letters - happens in same piece of code as 4
4.Build a list of letters to show, and display the string form - be able to guess letter; same as guess game
5.Create the win condition
keep track of what the user has actually guessed
when is it that the letter is revealed and when is it when the star is placed
if in letters guessed out put the answer
how to put a star '*'
Listform:{'_', '_' '_', '_', '_'}
    output = A _ _ _, _ _ _ _ __
    hidden_word = Anou, Leave
    guessesleft = 10
    letters_guessed =['a']
"""
