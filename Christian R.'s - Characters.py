# Characters
# 1. Name -
# 2.Description
# 3.Dialogue?
# 4.Inventory
# 5.Interact
# 6.Move
# 7.Climb
# 8.Look
# 9.Item
# 10.Fight
# 11.Health
# 12.takeDamage
# 13.Death
# 14.Stats
# something it has instance variable and something that it can do method
class Characterlmao(object):
    def __init__(self, item, description, name, stats):
        self.name = name
        self.description = description
        self.inventory = "Water, Banana, and Soda"
        self.item = item
        self.takedamage = False
        self.death = False
        self.stats = stats
        self.fight = False
        self.location = None  # A Room Object
        self.hp = 100
        self.maxHP = 100

    def if_die_lol(self):
        if self.death:
            print("you are alive lmao")
        else:
            print("you died lol")
            self.death = True

    def name_change_lmao(self):
            if input("no u"):
                    quit()

    def fighting(self):
        if self.fight:
            print("u are not fighting lmao")
        else:
            print("lol fighting lmao xd")
            self.fight = True

    def use_boost(self, boost_item):
        if self.hp == self.maxHP:
            print("You are already at full health.")
        else:
            boost_item.heal(self)

character1 = Characterlmao("Nothing","Black", "Jesus", "100000 hp lmao")
character1.fighting()
print(character1.fight)
character1.if_die_lol()
print(character1.death)
