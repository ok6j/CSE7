# yes = input("imstrighhat")
# 8 == yes
# print(8)

print(64**6)


def take_damage(self, amt):
    self.hp -= amt


def swing(self, target):
    target.take_damage(self.weapon)
    print('%s attacks %s' % (self.name, target.name))


def attack(self):
    target = Enemies
    target.take_damage(self.swing)
    print('%s attacks %s for %s' % (self.name, self.name, self.swing))
    if character1.hp <= 0:
        print('You died.')
        exit(0)
    if self.hp <= 0:
        target.death = True
        print('%s died.' % self.name)


def fight(self, enemy):
    if enemy == current_node.enemies:
        print(character1.name + ",", character1.description, "begins fighting with %s" % enemy.name + ",",
              enemy.description)
        while enemy.health > 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.hit(self)
            elif choice == enemy:
                self.swing(enemy)
        print()
    else:
        print("There's no enemy here only god.")


def use_boost(self, boost_item):
    if self.hp == self.max_hp:
        print("You are already at full health.")
    else:
        boost_item.heal(self)


def if_die_lol(self):
    if self.hp <= 0 or self.hp == 0:
        print("you died lmao")
        sys.exit(0)

    def swing(self, target):
        target.take_damage(self.weapon.damaged)
        print('%s attacks %s' % (self.name, target.name))

    def fight(self, enemy):
        print('You engage in a fight with the %s' % enemy.name)
        random.randit = ([Enemies], character1)
        first_strike = random.randint

        while self.hp >= 0 and Enemies.hp > 0:
            if input("fight"):
                if first_strike == Enemies:
                    Enemies.do_dmg(self)
                print('%s attacks you' % Enemies.name)
                if self.hp <= 0:
                    character1.die_lol()
                elif first_strike == self:
                    if self.weapon == 0:
                        print('You have no weapon to fight with, so you do no damage. The dinosaur easily kills you')
                    sys.exit(0)
                else:
                    self.swing(Enemies)
                    print('you attacked the %s' % Enemies.name)
                    if Enemies.hp <= 0:
                        print('The %s died' % Enemies.name)
