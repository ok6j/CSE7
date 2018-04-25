while self.hp >= 0 and Enemies.hp > 0:
    if input("fight"):
        if first_strike == Enemies:
            character1.take_damage(self)
        print('%s attacks you' % Enemies.name)
        if self.hp <= 0:
            character1.die_lol()
        elif first_strike == self:
            if self.weapon == 0:
                print('You have no weapon to fight with, so you do no damage.')
            sys.exit(0)
        else:
            self.swing(Enemies)
            print('you attacked the %s' % Enemies.name)
            if Enemies.hp <= 0:
                print('The %s died' % Enemies.name)