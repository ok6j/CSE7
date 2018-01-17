import random
num_of_rounds_total = 0
current_money = 15
best_round = 1
max_money = 15
while current_money > 0:
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    total = dice1 + dice2
    print("You rolled a", total)
    print("You now have %s dollars" % current_money)
    num_of_rounds_total += 1
    print("Round: %s" % best_round)
    if total == 7:
        current_money += 4
        if current_money > max_money:
            max_money = current_money
            best_round = num_of_rounds_total
    else:
        current_money -= 1
if current_money == 0:
    print("You've played %s rounds!" % num_of_rounds_total)
    if max_money < 15:
        print("You didn't gain or lose.")
    elif max_money > 14:
            print("You should've stopped at round %s when you had $%s" % (best_round, max_money))
