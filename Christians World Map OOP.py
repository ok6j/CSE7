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

east_shopkeeper_platform = Room("Shopkeeper Platform", 'northeast_inhibitor', None, 'southeast_inhibitor', None, None,
                                None, None, None, 'You are on a shopkeeper platform, he appears ecstatic.\n'
                       'There\'s two staircases one leading south and one leading north.',)

west_shopkeeper_platform = Room("Shopkeeper Platform", 'northeast_inhibitor', None, 'southeast_inhibitor', None, None,
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

purple_nexus = Room("purple_nexus", "northeast_inhibitor", None, 'southwest_inhibitor', None, None, None, None, None,)

blue_nexus = Room("blue_nexus", "northwest_inhibitor", None, 'southwest_ihibitor', None, None, None, None, None)

bottom_of_the_northeast_stairs = Room("bottom_of_the_northeast_stairs", "northeast_inhibitor", "northeast_jungle",
            "first_northeast_turrent", None, None, None, None, None, "Theres a jungle to the south.\n"
                                    "There appears to be a tower to the west and an inhibitor to the east.")

bottom_of_the_northwest_stairs = Room("bottom_of_the_northwest_stairs", "northwest_inhibitor", "northwest_jungle",
                        "first_northwest_turrent", None, None, None, None, None, 'Theres a jungle to the south.\n' 
                                    'There appears to be a tower to the east and an inhibitor to the west.')

bottom_of_the_southeast_stairs = Room("bottom_of_the_southeast_stairs", "southeast_inhibitor", "southeast_jungle",
                        "first_southeast_turrent", None, None, None, None, None, 'Theres a jungle to the north.\n' 
                                        'There appears to be a tower to the west and an inhibitor to the east.')

bottom_of_the_southwest_stairs = Room("bottom_of_the_southwest_stairs", "southwest_inhibitor", "southwest_jungle",
                        "first_southwest_turrent", None, None, None, None, None, 'Theres a jungle to the north.\n' 
              'There appears to be a tower to the east and an inhibitor to the west.')

northeast_jungle = Room("northeast_jungle", "bottom_of_the_northeast_stairs", "east_wolves_camp",
                        "first_northeast_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the northwest.\n'
                        'Theres a path to the south and a path to the north.')

northwest_jungle = Room("northwest_jungle", "bottom_of_the_northwest_stairs", "west_wolves_camp",
                        "first_northwest_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the northeast.\n'
                        'Theres a path to the south and a path to the north.')

southeast_jungle = Room("southeast_jungle", "bottom_of_the_southeast_stairs", "east_wraiths_camp",
                        "first_southeast_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the southwest.\n'
                        'Theres a path to the north and a path to the south.')

southwest_jungle = Room("southwest_jungle", "bottom_of_the_southwest_stairs", "west_wraiths_camp",
                        "first_southwest_turrent", None, None, None, None, None, 'Brush and vines crawl on the wall.\n'
                        'There appears to be a path to the southeast.\n'
                        'Theres a path to the north and a path to the south.')

east_golem_camp = Room("east_golem_camp", "east_altar", "northeast_jungle", "first_northeast_turrent", None, None,
                        None, None, None, 'You are met by 2 golems,one looking bigger than the other.\n'
                    'There\'s a path to the south and a path to the north.')

west_golem_camp = Room("west_golem_camp", "west_altar", "northwest_jungle", "first_northwest_turrent", None, None,
                        None, None, None, 'You are met by 2 golems,one looking bigger than the other.\n'
                    'There\'s a path to the south and the north.')

west_wolves_camp = Room("west_wolves_camp", "west-altar", None, None, None, None, None, None, None,
                        'You are met by 3 wolves, the biggest in the center.\n'
                        'There\'s a path to the north')

east_wolves_camp = Room("east_wolves_camp", "west-altar", None, None, None, None, None, None, None,
                        'You are met by 3 wolves, the biggest in the center.\n'
                        'There\'s a path to the north')

east_altar = Room("east_altar", "west_golem_camp", "first_southwest_turrent", "hp_pack", None, "second_northwest_turrent",
                  None, "west_wolves_camp", "west_wraiths_camp")

west_altar = Room("west_altar", "east_golem_camp", "first_southeast_turrent", "hp_pack", None, "second_northeast_turrent",
                  None, "east_wolves_camp", "east_wraiths_camp")

west_wraiths_camp = Room("west_wraiths_camp", "west_altar", "bottom_of_southwest_stairs", None, None, None, None, None,
                         None)

east_wraiths_camp = Room("east_wraiths_camp", "east_altar", "bottom_of_southeast_stairs", None, None, None, None, None,
                         None)

second_northeast_turrent = Room("second_northeast_turrent", "Vilemaw", "west_altar", "second_northwest_jungle",
                                "first_northeast_turrent", None, None, None, None)

second_southeast_turrent = Room("second_northeast_turrent", "west_altar", "second_northwest_jungle",
                                "first_northeast_turrent", None, None, None, None, None)

second_northwest_turrent = Room("second_northwest_turrent", "Vilemaw", "west_altar", "second_northwest_jungle",
                                "first_northwest_turrent", None, None, None, None)

second_southwest_turrent = Room("second_southwest_turrent", "west_altar", "second_southeast_jungle",
                                "first_southwest_turrent", None, None, None, None, None)

first_northeast_turrent = Room("first_northeast_turrent", "second_northeast_turrent", "east_jungle",
                               "bottom_of_the_northeast_stairs", None, None, None, None)

first_southeast_turrent = Room("first_southeast_turrent", "second_southeast_turrent",
                               "bottom_of_the_northeast_stairs", None, None, None, None)

first_northwest_turrent = Room("first_northwest_turrent", "second_northwest_turrent",
                               "bottom_of_the_northeast_stairs", None, None, None, None)

first_southwest_turrent = Room("first_southwest_turrent", "second_southwest_turrent",
                               "bottom_of_the_southwest_stairs", None, None, None, None)

Vilemaw = Room("Vilemaw", "second_northeast_turrent", "second_northwest_turrent", None, None, None, None, None, None)

hp_pack = Room("hp_pack", "west_altar" "east_altar", None, None, None, None, None, None, None)




current_node = Room
directions = ['north', 'south', 'northeast', 'east', 'southeast', 'west', 'southwest', 'northwest']
short_directions = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']

while True:
    print(current_node[Room])
    print(current_node[Room])
    command = input('>_ ').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
        *********
        except KeyError:
            print('You cannot go that way')
    else:
        print('command not recognized')
    print()
