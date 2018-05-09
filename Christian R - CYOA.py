import random


class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money


class Weapon(Item):
    def __init__(self, name, money, damage, description):
        super(Weapon, self).__init__(name, money)
        self.damage = damage
        self.description = description


class Consumable(Item):
    def __init__(self, heal, name, money):
        super(Consumable, self).__init__(name, money)
        self.heal = heal

    def heal(self):
        if Hppack in your_inv:
            print("You drink a %s" % self.name)
            self.heal += you.health
        else:
            print("You don't have any consumables.")


class Armor(Item):
    def __init__(self, name, health, money):
        super(Armor, self).__init__(name, money)
        self.health = health


class Dagger(Weapon):
    def __init__(self, name, money, damage, description):
        super(Dagger, self).__init__(name, money, damage, description)


class Longsword(Weapon):
    def __init__(self, name, money, damage, description):
        super(Longsword, self).__init__(name, money, damage, description)


class BlastingWand(Weapon):
    def __init__(self, name, money, damage, description):
        super(BlastingWand, self).__init__(name, money, damage, description)


class BFsword(Weapon):
    def __init__(self, name, money, damage, description):
        super(BFsword, self).__init__(name, money, damage, description)


class GuardianSword(Weapon):
    def __init__(self, name, money, damage, description):
        super(GuardianSword, self).__init__(name, money, damage, description)


class Hppack(Consumable):
    def __init__(self, heal, name, money, description):
        super(Hppack, self).__init__(heal, name, money)
        self.description = description


class FiendishCodex(Item):
    def __init__(self, name, money, description):
        super(FiendishCodex, self).__init__(name, money)
        self.description = description


class NullMagicMantle(Armor):
    def __init__(self, name, health, money):
        super(NullMagicMantle, self).__init__(name, health, money)


class BansheesVeil(Armor):
    def __init__(self, name, health, money):
        super(BansheesVeil, self).__init__(name, health, money)


class ClothArmor(Armor):
    def __init__(self, name, health, money):
        super(ClothArmor, self).__init__(name, health, money)


class ZzRotPortal(Item):
    def __init__(self, name, money, description):
        super(ZzRotPortal, self).__init__(name, money)
        self.description = description


class Stopwatch(Item):
    def __init__(self, name, money, description):
        super(Stopwatch, self).__init__(name, money)
        self.description = description


stopwatch = Stopwatch("Stopwatch", 0, "A broken stopwatch")
zzrotportal = ZzRotPortal("Zz'Rot Portal", "???", "A portal filled with nothingness.")
dagger = Dagger("Dagger", 1, 1, "A small dagger")
longsword = Longsword("Long Sword", 45, 100, "A long sword.")
blastingwand = BlastingWand("Blasting Wand", 15, 45, "It's a long spiked wand.")
bfsword = BFsword("B.F. Sword", 15, 15, "It's a blue tinted sword.")
guardiansword = GuardianSword("Guardian Sword", 200, 1000, "A sword with the feeling of life swarming it.")
hp_pack = Hppack(50, "Hp pack", 0, "Its an hp pack")
nullmagicmantle = NullMagicMantle("Null Magic Mantle", 15, 10)
bansheesveil = BansheesVeil("Banshees Veil", 100, 400)
clotharmor = ClothArmor("Cloth Armor", 3, 1)
fiendishcodex = FiendishCodex("Fiendish Codex", 2, "It's an item duh")


class Character(object):
    def __init__(self, name, health, description, attack, money, inventory):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.money = money
        self.inventory = inventory

    def take_damage(self, amount):
        self.health -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if you.health <= 0:
            print('You died.')
            exit(0)
        if target.health <= 0:
            print('%s died.' % target.name)
            print('You received %s gold.' % target.money)
            print('HP: %s' % you.health)
            self.money += target.money
            if target.health < 0:
                target.health = 0
            # Loot
            choice = random.randint(1, 20)
            loot = random.randint(1, 20)
            if choice == loot:
                your_inv.append(target.inventory)

    def fight(self, enemy):
        try:
            if enemy == current_node.enemy_in:
                print(you.name + ",", you.description, "starts fighting with %s" % enemy.name + ",", enemy.description)
                enemy.health = enemy.orig_hp
                while enemy.health != 0:
                    choice = random.choice([enemy, self])
                    if choice == self:
                        enemy.hit(self)
                        if you.health > max_hp:
                            you.health = max_hp
                    elif choice == enemy:
                        self.hit(enemy)
                print()
        except AttributeError:
            print("There's no enemy here.")


class Enemy(Character):
    def __init__(self, name, health, description, attack, inventory):
        super(Enemy, self).__init__(name, health, description, attack, 0, inventory)


class Room(object):
    def __init__(self, name, south, west, east, north, southwest, northeast, southeast, northwest, description,
                 enemy_in):
        self.name = name
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.southwest = southwest
        self.northeast = northeast
        self.southeast = southeast
        self.northwest = northwest
        self.description = description
        self.enemy_in = enemy_in

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


your_inv = []
max_hp = 100
you = Character("", 100, "", 10, 10000, your_inv)
east_Big_wolf = Enemy("East Big Wolf", 15, "A big menacing wolf", 15, clotharmor)
west_Big_wolf = Enemy("West Big Wolf", 25, "A big menacing wolf", 25,  bfsword)
east_Big_Wraiths = Enemy("East Big Wraith", 15, "Scary looking wraith", 15, nullmagicmantle)
west_Big_Wraiths = Enemy("West Big Wraith", 20, "Scary looking wraith", 10, stopwatch)
west_Big_Golem = Enemy('West Big Golem', 20, 'Big Golem', 20, blastingwand)
east_Big_Golem = Enemy('East Big Golem', 20, 'Big Golem', 20, fiendishcodex)
Vilemaw = Enemy('Vilemaw', 100, "A monsterous creature looms over you", 100, ZzRotPortal)


east_shopkeeper_platform = Room("Shopkeeper Platform", 'northeast_inhibitor', 'southeast_inhibitor', None, None, None,
                                None, None, None, 'You are on a shopkeeper platform, he appears ecstatic.\n'
                                'There\'s two staircases one leading south and one leading west.', None)

west_shopkeeper_platform = Room("Shopkeeper Platform", 'northeast_inhibitor', 'southeast_inhibitor', None, None, None,
                                None, None, None, 'You are on a shopkeeper platform, he appears ecstatic.\n'
                                'There\'s two staircases one leading south and one leading west.', None)

southeast_inhibitor = Room("Southeast Inhibitor", "bottom_of_the_southeast stairs", "east_shopkeeper_platform",
                           "purple_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go east and north.", None)

southwest_inhibitor = Room("Southwest Inhibitor", "bottom_of_the_southwest stairs", "west_shopkeeper_platform",
                           "purple_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go west and north.", None)

northeast_inhibitor = Room("Northeast Inhibitor", "bottom_of_the_northeast_stairs", "east_shopkeeper_platform",
                           "purple_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go south, west, and east.", None)

northwest_inhibitor = Room("Northwest Inhibitor", "bottom_of_the_northwest_stairs", "west_shopkeeper_platform",
                           "blue_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go west and north.", None)

purple_nexus = Room("Purple Nexus", "northeast_inhibitor", None, 'southwest_inhibitor', None, None, None, None, None,
                    "A big purple crystal, it appears you can go south and east.", None)

blue_nexus = Room("Blue nexus", "northwest_inhibitor", None, 'southwest_ihibitor', None, None, None, None, None,
                  "A big blue crystal, you can go south and east", None)

bottom_of_the_northeast_stairs = Room("Bottom of the Northeast Stairs", "northeast_inhibitor", "northeast_jungle",
                                      "first_northeast_turrent", None, None, None, None, None,
                                      "There\'s a jungle to the south.\n"
                                      "There appears to be a tower to the west and an inhibitor to the east.", None)

bottom_of_the_northwest_stairs = Room("Bottom of the Northwest Stairs", "northwest_inhibitor", "northwest_jungle",
                                      "first_northwest_turrent", None, None, None, None, None,
                                      'There\'s a jungle to the south.\n' 
                                      'There appears to be a tower to the east and an inhibitor to the west.', None)

bottom_of_the_southeast_stairs = Room("Bottom of the Southeast Stairs", "southeast_inhibitor", "southeast_jungle",
                                      "first_southeast_turrent", None, None, None, None, None,
                                      'There\'s a jungle to the north.\n' 
                                      'There appears to be a tower to the west and an inhibitor to the east.', None)

bottom_of_the_southwest_stairs = Room("Bottom of the Southwest Stairs", "southwest_inhibitor", "southwest_jungle",
                                      "first_southwest_turrent", None, None, None, None, None,
                                      'There\'s a jungle to the north.\n'
                                      'There appears to be a tower to the east and an inhibitor to the west.', None)

northeast_jungle = Room("Northeast Jungle", "bottom_of_the_northeast_stairs", "east_wolves_camp",
                        "first_northeast_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the northwest.\n'
                        'There\'s a path to the south and a path to the north.', None)

northwest_jungle = Room("Northwest Jungle", "bottom_of_the_northwest_stairs", "west_wolves_camp",
                        "first_northwest_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the northeast.\n'
                        'There\'s a path to the south and a path to the north.', None)

southeast_jungle = Room("Southeast Jungle", "bottom_of_the_southeast_stairs", "east_wraiths_camp",
                        "first_southeast_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the southwest.\n'
                        'There\'s a path to the north and a path to the south.', None)

southwest_jungle = Room("Southwest Jungle", "bottom_of_the_southwest_stairs", "west_wraiths_camp",
                        "first_southwest_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the southeast.\n'
                        'There\'s a path to the north and a path to the south.', None)

east_golem_camp = Room("East Golem Camp", "east_altar", "northeast_jungle", "first_northeast_turrent", None, None,
                       None, None, None, 'You are met by 2 golems,one looking bigger than the other.\n'
                       'There\'s a path to the south and a path to the north.', east_Big_Golem)

west_golem_camp = Room("West Golem Camp", "west_altar", "northwest_jungle", "first_northwest_turrent", None, None,
                       None, None, None, 'You are met by 2 golems,one looking bigger than the other.\n'
                       'There\'s a path to the south and the north.', west_Big_Golem)

west_wolves_camp = Room("West Wolves Camp", "east-altar", None, None, None, None, None, None, None,
                        'You are met by 3 wolves, the biggest in the center.\n'
                        'There\'s a path to the north', west_Big_wolf)

east_wolves_camp = Room("East Wolves Camp", "west-altar", None, None, None, None, None, None, None,
                        'You are met by 3 wolves, the biggest in the center.\n'
                        'There\'s a path to the north', east_Big_wolf)

east_altar = Room("East Altar", "west_golem_camp", "first_southwest_turrent", "hp_pack", None,
                  "second_northwest_turrent", None, "west_wolves_camp", "west_wraiths_camp", "An altar of souls.", None)

west_altar = Room("West Altar", "east_golem_camp", "first_southeast_turrent", "hp_pack", None,
                  "second_northeast_turrent", None, "east_wolves_camp", "east_wraiths_camp", "An altar of souls.", None)

west_wraiths_camp = Room("West Wraiths Camp", "west_altar", "bottom_of_southwest_stairs", None, None, None, None, None,
                         None, "You are met with 3 wraiths", west_Big_Wraiths)

east_wraiths_camp = Room("East Wraiths Camp", "east_altar", "bottom_of_southeast_stairs", None, None, None, None, None,
                         None, "You are met with 3 wraiths", east_Big_Wraiths)

second_northeast_turrent = Room("Second Northeast Turrent", "Vilemaw", "west_altar", "second_northwest_jungle",
                                "first_northeast_turrent", None, None, None, None, "Its a turrent", None)

second_southeast_turrent = Room("Second Northeast Turrent", "west_altar", "second_northwest_jungle",
                                "first_northeast_turrent", None, None, None, None, None, "Its a turrent", None)

second_northwest_turrent = Room("Second Northwest Turrent", "Vilemaw", "west_altar", "second_northwest_jungle",
                                "first_northwest_turrent", None, None, None, None, "Its a turrent", None)

second_southwest_turrent = Room("Second Southwest Turrent", "west_altar", "second_southeast_jungle",
                                "first_southwest_turrent", None, None, None, None, None, "Its a turrent", None)

first_northeast_turrent = Room("First Northeast Turrent", "second_northeast_turrent", "east_jungle",
                               "bottom_of_the_northeast_stairs", None, None, None, None, None, "Its a turrent", None)

first_southeast_turrent = Room("First Southeast Turrent", "second_southeast_turrent",
                               "bottom_of_the_northeast_stairs", None, None, None, None, None, None, "Its a turrent.",
                               None)

first_northwest_turrent = Room("First Northwest Turrent", "second_northwest_turrent",
                               "bottom_of_the_northeast_stairs", None, None, None, None, None, None, "Its a turrent.",
                               None)

first_southwest_turrent = Room("First Southwest Turrent", "second_southwest_turrent",
                               "bottom_of_the_southwest_stairs", None, None, None, None, None, None, "Its a turrent.",
                               None)

Vilemaw_Room = Room("Vilemaw Room", "second_northeast_turrent", "second_northwest_turrent", None, None, None, None,
                    None, None, "Big monster spider lmao", Vilemaw)

hp_room = Room("Hp Room", "west_altar" "east_altar", None, None, None, None, None, None, None, "Pack of hp", None)

ZzRotPortal_Room = Room("Portal Room", None, None, None, None, None, None, None, None, "A dark nothingness.", you)

current_node = east_shopkeeper_platform
directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
short_directions = ['se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne']
all_the_commands = ['buy', 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast',
                    'se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne', 'hp', 'money', 'help', 'inv', 'fight', 'stats', 'me',
                    'sell', 'buy', 'heal']

character_name = input('What do you want to be named?\n>_')
you.name = character_name
character_description = input('How would you describe yourself?\na:')
you.description = character_description

while True:
    print(current_node.name)
    print(current_node.description)

    command = input('>_ ').lower().strip()

    if command == 'heal':
        if hp_pack in your_inv:
            if you.health == max_hp:
                print("You are already full hp.")
            if you.health < max_hp:
                print("You drink a health potion.")
                you.health += hp_pack.heal
                if you.health > max_hp:
                    you.health = max_hp
            print('HP: %s' % you.health)
        else:
            "You don\'t have a health potion."
        if hp_pack not in your_inv:
            print("You don\'t have a health potion.")

    if command == 'hp':
        print(str(you.health)+'/'+str(max_hp))

    if command == 'stats':
        print('-------------------------------')
        print('MAX HP' + ' - ' + str(max_hp))
        print('ATT' + ' - ' + str(you.attack))
        print('-------------------------------')

    if command == 'me':
        print('-------------------------------')
        print(you.name)
        print(you.description)
        print('-------------------------------')

    if command == 'buy':
        armor_shop = [bansheesveil]
        weapon_shop = [longsword, guardiansword]
        shop = [bansheesveil, longsword, guardiansword]

        if current_node == east_shopkeeper_platform:
            print("---SHOP---"
                  "\nBANSHEES VEIL(0)------ 400G"
                  "\nLONG SWORD(1)---------- 20G"
                  "\nGUARDIAN SWORD(2)-------- 200G"
                  "\n----------")
            item_buying = input("What do you want to buy? (Type in the number)\nYOUR MONEY: %s\n>_" % you.money)
            try:
                item_buy = shop[int(item_buying)]
                if you.money < item_buy.money:
                    print("You're poor.")
                if you.money >= item_buy.money:
                    print("You buy a %s." % item_buy.name)
                    your_inv.append(item_buy)
                    you.money -= item_buy.money
                    if item_buy in armor_shop:
                        max_hp += item_buy.health
                    if item_buy in weapon_shop:
                        you.attack += item_buy.damage
            except ValueError:
                print("That is not an item.")
            except IndexError:
                print("That is not an item")
        elif current_node != east_shopkeeper_platform:
            print('You are at the shopkeeper platform.')

    if command == 'sell':
        armor_shop = [clotharmor, bansheesveil, nullmagicmantle]
        weapon_shop = [bfsword, blastingwand, guardiansword, longsword, dagger]
        shop = [clotharmor, bansheesveil, nullmagicmantle, bfsword, blastingwand, guardiansword, longsword, dagger,
                hp_pack]

        if current_node == east_shopkeeper_platform:
            for i in your_inv:
                print('YOUR INV:')
                print('[ ' + i.name + ' ]')
            if len(your_inv) == 0:
                print([])
            print("\nCLOTH ARMOR(0)"
                  "\nBANSHEES VEIL(1)"
                  "\nNULL MAGIC MANTLE(2)"
                  "\nB.F. SWORD(3)"
                  "\nBLASTING WAND(4)"
                  "\nGUARDIAN SWORD(5)"
                  "\nLONG SWORD(6)"
                  "\nDAGGER(7)"
                  "\nHP PACK(8)"
                  "\n----------")
            selling = input('What do you want to sell?')
            try:
                sold = shop[int(selling)]
                if sold not in your_inv:
                    print('You don\'t have this in your inventory.')
                if sold in your_inv:
                    print('You sell a %s.' % sold.name)
                    you.money += sold.money
                    your_inv.remove(sold)
                    you.money += sold.money
                    if sold in armor_shop:
                        max_hp -= sold.health
                    if sold in weapon_shop:
                        you.attack -= sold.damage
            except ValueError:
                print('That is not an option.')

    if command == 'quit':
        exit(0)

    if command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]

    if command == 'money':
        print(you.money)

    if command == 'help':
        print("Type 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast', 'se', 'nw', "
              "'s', 'w', 'e', 'n', 'sw', 'ne' to move.")

    if command == 'inv':
        for i in your_inv:
            print('[ ' + i.name + ' ]')
        if len(your_inv) == 0:
            print([])

    if command == 'fight':
        you.fight(current_node.enemy_in)

    if command == 'shrek':
        print("You become vilemaw.")
        exit(0)

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
        except AttributeError:
            print("You cannot leave.")
    elif command not in all_the_commands:
        print("Command not found.")

    print("---------------------------------------------------------------------------------------------------------"
          "-----------------------------------------")
    print()
