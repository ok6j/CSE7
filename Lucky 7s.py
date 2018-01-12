import random
played = 0
money = 15
rounds = 0
highest = 15
while money > 0:
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    total = dice1 + dice2
    print("You rolled a", total)
    print("You now have %s dollars" % money)
    print("Round: %s" % rounds)
    if total == 7:
        money += 4
        if money > highest:
            money = highest
            (played): rounds
    else:
        money -= 1
        rounds += 1
    if money == 0:
            print("You shouldve have stopped at round: %s when you had %s money"(rounds, highest))

