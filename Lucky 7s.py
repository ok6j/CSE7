import random
dice1 = (random.randint(1, 6))

dice2 = (random.randint(1, 6))

money = 15

while money > 0:
    total = dice1 + dice2
    print("You rolled a", total)


