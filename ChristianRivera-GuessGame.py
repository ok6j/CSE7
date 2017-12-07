import random
# Christian Rivera

print("I'm guessing a number between 1-50")
you_belong_in_a_museum = (random.randint(1, 50))


for x in range(5):
    b = input("What number am I thinking of? ")
    if b == str(you_belong_in_a_museum):
        print("Correct")
        quit()
    elif b > str(you_belong_in_a_museum):
        print("Lower")
    elif b < str(you_belong_in_a_museum):
        print("Higher")




# Generate a random number between one and 50
# Get a number (input) from the user
# Compare the number to input  #Operators and Recasters say true if its the same say false if not
# add "higher or "lower" operators
# add 5 guesses
# make a variable to count the number of guesses says 5 guesses goes down
