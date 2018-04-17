# 1.Import statements
# 2.Class Definitions
# 3.a Items
# 3.b Characters
# 3.c Rooms
# 4.Instantiation of classes
# 5. Controller
inventory = None


class Item(object):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.used = False
        self.value = value

    def use(self):
        if self.used:
            print("usable")
        else:
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
    def __init__(self, name, description, value, defense):
        super(Armor, self).__init__(name, description, value)
        self.defense = defense


class Boosts(Item):
    def __init__(self, buff):
        super(Boosts, self).__init__(self.name, self.description, self.value)
        self.buff = buff

    def buffed(self):
        if self.buff:
            print("You are buffed with %s" % self.buff.name)

        else:
            print("You are not buffed")


class HpBoosts(Item):
    def __init__(self, healing):
        super(HpBoosts, self).__init__("Hp boost", "Its a green cross and its glowing", "Nothing")
        self.healing = healing

    def heal(self, character):
        character.hp += self.healing


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Dagger", "Its a dagger", "Nothing, like you", 1)


class LongSword(Weapon):
    def __init__(self):
        super(LongSword, self).__init__("Long Sword", "Its a long boi", "350 gold", 56)


class BlastingWand(Weapon):
    def __init__(self):
        super(BlastingWand, self).__init__("Blasting Wand", "Its a wand", "32 gold", 32)


class BFSword(Weapon):
    def __init__(self):
        super(BFSword, self).__init__("B.F. Sword", "It's a big sword lmao", "43 gold", 32)


class GuardianSword(Weapon):
    def __init__(self, revive):
        super(GuardianSword, self).__init__("Guardian Sword", "Its shiny and sharp", "200 gold", 100)
        self.revive = revive

    def liveagain(self, character):
        if character1.die_lol:
            if GuardianSword in inventory:
                character.location = east_shopkeeper_platform  # Defined as a room


class ClothArmor(Armor):
    def __init__(self):
        super(ClothArmor, self).__init__("Cloth Armor", "Its clothy and stuff", "nothing", 2.5)


class NullMagicMantle(Armor):
    def __init__(self):
        super(NullMagicMantle, self).__init__("Null_Magic_Mantle", "It's a metal skirt", "2", 17)


class BansheesVeil(Armor):
    def __init__(self, block):
        super(BansheesVeil, self).__init__("Bnashees_Veil", "It's a necklace", "300 gold", 100)
        self.block = block

    def passive(self):
        if self.block:
            print("A shield surrounds you and blocks all damage")
            Vilemaw.totaldamage = 0
        else:
            print()


class ZzRotPortal(Item):
    def __init__(self):
        super(ZzRotPortal, self).__init__("Zz'Rot Portal", "A rock encrusted void", 350)


nigerian = Weapon("Nigerian", "Whatever", 100, 9)
item1 = ZzRotPortal()
item2 = nigerian
stopwatch = Item("stopwatch", "Its a broken stopwatch", 1)
fiendish_codex = Item("Fiendish Codex", "a large glowing book", 3)

print(item2.description)


class Characterlmao(object):
    def __init__(self, item, description, name, hp, defense,):
        self.name = name
        self.description = description
        self.inventory = [item]
        self.takedamage = False
        self.death = False
        self.max_hp = 100
        self.max_defense = 100
        self.hp = hp
        self.defense = defense
        self.fight = False
        self.location = None  # A Room Object

    def die_lol(self):
        if character1.hp == 0:
            print("you died lmao")
            exit(0)

    def fighting(self):
        if input("fight"):
            if enemies != Room:
                print("you are fighting nothing")
        else:
            print("lol fighting lmao xd")
            self.fight = True
            if character1.inventory != LongSword in west_wolves_camp:
                character1.die_lol()
            else:
                if enemies.hp == 0:
                    enemies.die_lol()
            if character1.inventory != LongSword in east_wolves_camp:
                character1.die_lol()
            if character1.inventory != BFSword in west_Big_Golem:
                character1.die_lol()
                if character1.hp(self):
                    character1.die_lol()

    def use_boost(self, boost_item):
        if self.hp == self.max_hp:
            print("You are already at full health.")
        else:
            boost_item.heal(self)


class enemies(Characterlmao):
    def __init__(self, inventory, description, name, hp, defense):
        super(enemies, self).__init__(inventory, description, name, hp, defense)


class Vilemaw(enemies):
    def __init__(self):
        super(Vilemaw, self).__init__([ZzRotPortal], "A large spider looking creature", "Vilemaw", 100, 100)


character1 = Characterlmao(None, "Black", "Jesus", 10, 12)
character1.fighting()
print(character1.fight)
character1.die_lol()
print(character1.death)
east_Big_wolf = Characterlmao(ClothArmor, "Big monsterous looking wolf", "Large Wolf", 14, 16)
west_Big_wolf = Characterlmao(BFSword, "Big monsterous looking wolf", "Large Wolf", 14, 16)
east_Big_Wraiths = Characterlmao(NullMagicMantle, "Scary looking wraith", "Big_Wraith", 13, 14)
west_Big_Wraiths = Characterlmao(stopwatch, "Scary looking wraith", "Big_Wraith", 13, 14)
west_Big_Golem = Characterlmao(BlastingWand, "A huge golem", "Big Golem", 13, 14)
east_Big_Golem = Characterlmao(fiendish_codex, "A huge golem", "Big Golem", 13, 14)


class Room(object):
    def __init__(self, name, north, south, west, east, northeast, northwest, southeast, southwest, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# west_house = Room("West of House", 'north_house')
# north_house = Room("North of House", None)

east_shopkeeper_platform = Room("Shopkeeper Platform", 'northeast_inhibitor', 'southeast_inhibitor', None, None, None,
                                None, None, None, 'You are on a shopkeeper platform, he appears ecstatic.\n'
                                'There\'s two staircases one leading south and one leading north.',)

west_shopkeeper_platform = Room("Shopkeeper Platform", 'northeast_inhibitor', 'southeast_inhibitor', None, None, None,
                                None, None, None, 'You are on a shopkeeper platform, he appears ecstatic.\n'
                                'There\'s two staircases one leading south and one leading north.')

southeast_inhibitor = Room("southeast_inhibitor", "bottom_of_the_southeast stairs", "east_shopkeeper_platform",
                           "purple_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go east and north.")

southwest_inhibitor = Room("southwest_inhibitor", "bottom_of_the_southwest stairs", "west_shopkeeper_platform",
                           "blue_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go west and north.")

northeast_inhibitor = Room("northeast_inhibitor", "bottom_of_the_northeast_stairs", "east_shopkeeper_platform",
                           "purple_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go east and north.")

northwest_inhibitor = Room("northwest_inhibitor", "bottom_of_the_northwest_stairs", "west_shopkeeper_platform",
                           "blue_nexus", None, None, None, None, None, "You are next to a giant crystal.\n" 
                           "It appears you can go west and north.")

purple_nexus = Room("purple_nexus", "northeast_inhibitor", None, 'southwest_inhibitor', None, None, None, None, None,
                    "A big purple crystal")

blue_nexus = Room("blue_nexus", "northwest_inhibitor", None, 'southwest_ihibitor', None, None, None, None, None,
                  "A big blue crystal")

bottom_of_the_northeast_stairs = Room("bottom_of_the_northeast_stairs", "northeast_inhibitor", "northeast_jungle",
                                      "first_northeast_turrent", None, None, None, None, None,
                                      "There\'s a jungle to the south.\n"
                                      "There appears to be a tower to the west and an inhibitor to the east.")

bottom_of_the_northwest_stairs = Room("bottom_of_the_northwest_stairs", "northwest_inhibitor", "northwest_jungle",
                                      "first_northwest_turrent", None, None, None, None, None,
                                      'There\'s a jungle to the south.\n' 
                                      'There appears to be a tower to the east and an inhibitor to the west.')

bottom_of_the_southeast_stairs = Room("bottom_of_the_southeast_stairs", "southeast_inhibitor", "southeast_jungle",
                                      "first_southeast_turrent", None, None, None, None, None,
                                      'There\'s a jungle to the north.\n' 
                                      'There appears to be a tower to the west and an inhibitor to the east.')

bottom_of_the_southwest_stairs = Room("bottom_of_the_southwest_stairs", "southwest_inhibitor", "southwest_jungle",
                                      "first_southwest_turrent", None, None, None, None, None,
                                      'There\'s a jungle to the north.\n'
                                      'There appears to be a tower to the east and an inhibitor to the west.')

northeast_jungle = Room("northeast_jungle", "bottom_of_the_northeast_stairs", "east_wolves_camp",
                        "first_northeast_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the northwest.\n'
                        'There\'s a path to the south and a path to the north.')

northwest_jungle = Room("northwest_jungle", "bottom_of_the_northwest_stairs", "west_wolves_camp",
                        "first_northwest_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the northeast.\n'
                        'There\'s a path to the south and a path to the north.')

southeast_jungle = Room("southeast_jungle", "bottom_of_the_southeast_stairs", "east_wraiths_camp",
                        "first_southeast_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the southwest.\n'
                        'There\'s a path to the north and a path to the south.')

southwest_jungle = Room("southwest_jungle", "bottom_of_the_southwest_stairs", "west_wraiths_camp",
                        "first_southwest_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the southeast.\n'
                        'There\'s a path to the north and a path to the south.')

east_golem_camp = Room("east_golem_camp", "east_altar", "northeast_jungle", "first_northeast_turrent", None, None,
                       None, None, None, 'You are met by 2 golems,one looking bigger than the other.\n'
                       'There\'s a path to the south and a path to the north.')

west_golem_camp = Room("west_golem_camp", "west_altar", "northwest_jungle", "first_northwest_turrent", None, None,
                       None, None, None, 'You are met by 2 golems,one looking bigger than the other.\n'
                       'There\'s a path to the south and the north.')

west_wolves_camp = Room("west_wolves_camp", "east-altar", None, None, None, None, None, None, None,
                        'You are met by 3 wolves, the biggest in the center.\n'
                        'There\'s a path to the north')

east_wolves_camp = Room("east_wolves_camp", "west-altar", None, None, None, None, None, None, None,
                        'You are met by 3 wolves, the biggest in the center.\n'
                        'There\'s a path to the north')

east_altar = Room("east_altar", "west_golem_camp", "first_southwest_turrent", "hp_pack", None,
                  "second_northwest_turrent", None, "west_wolves_camp", "west_wraiths_camp", "An altar of souls.")

west_altar = Room("west_altar", "east_golem_camp", "first_southeast_turrent", "hp_pack", None,
                  "second_northeast_turrent", None, "east_wolves_camp", "east_wraiths_camp", "An altar of souls.")

west_wraiths_camp = Room("west_wraiths_camp", "west_altar", "bottom_of_southwest_stairs", None, None, None, None, None,
                         None, "You are met with 3 wraiths")

east_wraiths_camp = Room("east_wraiths_camp", "east_altar", "bottom_of_southeast_stairs", None, None, None, None, None,
                         None, "You are met with 3 wraiths")

second_northeast_turrent = Room("second_northeast_turrent", "Vilemaw", "west_altar", "second_northwest_jungle",
                                "first_northeast_turrent", None, None, None, None, "Its a turrent")

second_southeast_turrent = Room("second_northeast_turrent", "west_altar", "second_northwest_jungle",
                                "first_northeast_turrent", None, None, None, None, None, "Its a turrent")

second_northwest_turrent = Room("second_northwest_turrent", "Vilemaw", "west_altar", "second_northwest_jungle",
                                "first_northwest_turrent", None, None, None, None, "Its a turrent")

second_southwest_turrent = Room("second_southwest_turrent", "west_altar", "second_southeast_jungle",
                                "first_southwest_turrent", None, None, None, None, None, "Its a turrent")

first_northeast_turrent = Room("first_northeast_turrent", "second_northeast_turrent", "east_jungle",
                               "bottom_of_the_northeast_stairs", None, None, None, None, None, "Its a turrent")

first_southeast_turrent = Room("first_southeast_turrent", "second_southeast_turrent",
                               "bottom_of_the_northeast_stairs", None, None, None, None, None, None, "Its a turrent.")

first_northwest_turrent = Room("first_northwest_turrent", "second_northwest_turrent",
                               "bottom_of_the_northeast_stairs", None, None, None, None, None, None, "Its a turrent.")

first_southwest_turrent = Room("first_southwest_turrent", "second_southwest_turrent",
                               "bottom_of_the_southwest_stairs", None, None, None, None, None, None, "Its a turrent.")

Vilemaw_Room = Room("Vilemaw_Room", "second_northeast_turrent", "second_northwest_turrent", None, None, None, None,
                    None, None, "Big monster spider lmao")

hp_pack = Room("hp_pack", "west_altar" "east_altar", None, None, None, None, None, None, None, "Pack of hp")


current_node = east_shopkeeper_platform
directions = ['north', 'south', 'northeast', 'east', 'southeast', 'west', 'southwest', 'northwest']
short_directions = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        location = short_directions.index(command)
        command = directions[location]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('You can\'t go this way')
    else:
        print('command not recognized')
    if current_node == ZzRotPortal:
        print("The void consumes you, you become Vilemaw")
        exit(0)
