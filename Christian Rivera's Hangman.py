import random

word_bank = ["Graves", "Talon", "Nasus", "Darius", "Diana", "Garen", "Taric", "Yasuo", "Jhin", "Ziggs"]
for characters in word_bank:
    print()


"""
Outline of Hangman
1. Make a word bank - 10 items
2.select a random item from the list - going to be the word you're going to guess
3.Hide the word (use *) - happens in same piece of code as 4
4.Reveal letters if they have been guessed - be able to guess letter; same as guess game
5.Create the win condition
keep track of what the user has actually guessed
when is it that the letter is revealed and when is it when the star is placed
"""
