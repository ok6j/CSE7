import random
# Christian Rivera
you_belong_in_a_museum = (random.randint(1, 50))

print(you_belong_in_a_museum)
print("Im thinking of a number between 1-50 ")
number = input("What number am I thinking of?")
print(number == str(you_belong_in_a_museum))
guess = 5

while int(guess) != you_belong_in_a_museum:
    if int(guess) == you_belong_in_a_museum:
        print("Correct")
    elif int(guess) > you_belong_in_a_museum:
        print("Lower")
    elif int(guess) < you_belong_in_a_museum:
        print("Higher")




# Generate a random number between one and 50
# Get a number (input) from the user
# Compare the number to input  #Operators and Recasters say true if its the same say false if not
# add "higher or "lower" operators
# add 5 guesses
# make a variable to count the number of guesses says 5 guesses goes down
