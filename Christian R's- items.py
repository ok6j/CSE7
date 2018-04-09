inventory = ("nothing")
class Item(object):
    def __init__ (self, name, description, value):
        self.name = name
        self.description = description
        self.used = False
        self.value = value

    def use(self):
        if self.used:
            print("usable")
        else:
            inventory.remove
            self.used = True

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super(Weapon, self).__init__(name, description, value)
        self.damage = damage

    def do_damage(self, player):
        if self.damage:
            print("You did %s damage" % player.totaldamage)
        else:
            print("You did no damage lmao")

class Armor(Item):
    def __init__(self, defense):
        super(Armor, self).__init__(name, description, value)
        self.defense = defense


class Gold(Item):
    def __init__(self, name, description, value, currency):
        super(Gold, self).__init__(name, description, value)
        self.currency = currency

    def buy(self):
        if self.currency:
            print("You bough %s for %c" % self.item % self.currency)

    def sell(self):
        if self.currency:
            print("You gained %s" % self.value)
            self.currency =+ self.value

class Boosts(Item):
    def __init__(self, buff):
        super(Boosts, self).__init__(self.name, self.description, self.value)
        self.buff = buff

    def buffed(self):
        if self.buff:
            print("You are buffed with %s"% self.buff.name)

        else:
            print("You are not buffed")

class Hp_Boosts(Item):
    def __init__(self, healing):
        super(Hp_Boosts, self).__init__("Hp boost", "Its a green cross and its glowing", "Nothing")
        self.healing = healing

    def healed(self):
        if self.healing:
            self.healing =+ self.hp
            if self.maxhp:
                self.maxhp = 100
                print("You're already max hp.")

class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Dagger", "Its a dagger", "Nothing, like you")

class Long_Sword(Weapon):
    def __init__(self):
        super(Long_Sword, self).__init__("Long Sword", "Its a long boi", "350 gold")

class Blasting_Wand(Weapon):
    def __init__(self):
        super(Blasting_Wand, self).__init__("Blasting Wand", "Its a wand", "32 gold")

class BF_Sword(Weapon):
    def __init__(self):
        super(BF_Sword, self).__init__("B.F. Sword", "It's a big sword lmao", "43 gold")

class Guardian_Sword(Weapon):
    def __init__(self, revive):
        super(Guardian_Sword, self).__init__("Guardian Sword", "Its shiny and sharp", "200 gold")
        self.revive = revive

    def liveagain(self, character):
        character.location = shopkeeper_platform  # Defined as a room

class Cloth_Armor(Armor):
    def __init__(self):
        super(Cloth_Armor, self).__init__("Cloth Armor", "Its clothy and stuff", "nothing")

class Null_Magic_Mantle(Armor):
    def __init__(self):
        super(Null_Magic_Mantle, self).__init__("Null_Magic_Mantle", "It's a metal skirt", "2")

class Banshees_Veil(Armor):
    def __init__(self, block):
        super(Banshees_Veil, self).__init__("Bnashees_Veil","It's a necklace", "300 gold")
        self.block = block

    def passive(self):
        if self.block:
            print("A shield surrounds you and blocks all damage")
            self.Vilemaw.totalDamage = 0
        else:
            print()

class ZzRot_Portal(Item):
    def __init__(self):
        super(ZzRot_Portal, self).__init__("Zz'Rot Portal", "A rock encrusted void", 350)


nigerian = Weapon("Nigerian", "WHatever", 100, 9)
item1 = ZzRot_Portal()
item2 = nigerian

print(item2.description)