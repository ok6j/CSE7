# world_map = {
#     'WESTHOUSE':{
#         'NAME': 'WEST OF HOUSE',
#         'DESCRIPTION': 'You are west of a small house',
#         'PATHS': {
#             'NORTH': "NORTHHOUSE",
#             'SOUTH': "SOUTHHOUSE"
#         }
#     },
#     'NORTHHOUSE': {
#         'NAME':'NORTH OF HOUSE',
#         'DESCRIPTION': 'Insert description here',
#         'PATHS':{
#             'WEST':'WESTHOUSE',
#         }
#     },
#     'SOUTHHOUSE': {
#         'NAME':'SOUTH OF HOUSE',
#         'DESCRIPTION': 'Insert description here',
#         'PATHS': {
#             'WEST':'WESTHOUSE'
#         }
#     }
# }
#
# current_node = world_map["SOUTHHOUSE"]
# print(current_node["NAME"])
# print(current_node["DESCRIPTION"])
twisted_treeline = {
    'Shopkeeper Platform': {
        'NAME': 'Shopkeeper Platform',
        'Description': 'You are on a shopkeeper platform, he appears estatic.\n'
                       'There\'s two staircases one leading south and one leading north.',
    }
}
'''
'NAME': 'South Inhibitor',
'Description':"You are next to a giant crystal."
              "It seems like you can go North."

'NAME': 'North Inhibitor',
'Description': "You are next to a giant crystal." 
               "It appears you can go west."

'NAME': 'Bottom of the North Stairs'
'Description':"Theres a jungle to the south." \
              "There appears to be a tower to the west."

'NAME': 'Bottom of the South Stairs'
'Description':"Theres a jungle to the north." \
              "There appears to be a tower to the west."

'NAME': 'The West Jungle'
'Description':"Brush and vines crawl on the wall."
                "There appears to be a path to the south"
                "Theres a path to the northwest"
                
'NAME': 'The East Jungle'
'Description':"Brush and vines crawl on the wall."
                "There appears to be a path to the north"
                "Theres a path to the southwest"

'NAME': 'East Golem Camp'
'Description':"You are met by 2 golems,one looking bigger than the other."
                "Theres a path to the south."
                
'NAME': 'West Golem Camp'
'Description':"You are met by 2 golems,one looking bigger than the other."
                "Theres a path to the south."
                
'NAME': 'East Altar'
'Description':"You see an altar filled with souls"
                "You can go Northeast,southwest,southeast and south

'NAME': 'West Altar'
'Description':"You see an altar filled with souls"
                "You can go Northeast,southwest,southeast and south"

'NAME': 'East Wolves Camp'
'Description':"3 wolves look viciously at you,the one in the middle looking bigger than the rest"
                
'NAME':'

'NAME': 'West Wolves Camp'
'Description':"3 wolves look viciously at you,the on in the middle looking bigger than the rest"
print(twisted_treeline['Shopkeeper Platform']['Description'])'''

world_map = {
    'Shopkeeper Platform': {
        'NAME': 'Purple Shopkeeper Platform',
        'DESCRIPTION': 'You are on a shopkeeper platform, he appears ecstatic.\n'
                       'There\'s two staircases one leading south and one leading north.',
        'PATHS': {
            'NORTH': "Northeast Inhibitor",
            'SOUTH': "Southwest Inhibitor"
        }
    },
    'Northeast Inhibitor': {
        'NAME': 'Northeast Inhibitor',
        'DESCRIPTION': "You are next to a giant crystal.\n" 
                        "It appears you can go west.",
        'PATHS': {
            'SOUTHEAST': 'Purple Shopkeeper Platform',
            'SOUTH': 'PURPLE NEXUS'
        }
    },
    'Southeast Inhibitor': {
        'NAME': 'Southeast Inhibitor',
        'DESCRIPTION': 'You are next to a giant crystal.\n'
                        'It appears you can go east',
        'PATHS': {
             'East': 'PURPLE NEXUS',
            'NORTHWEST': 'PURPLE Shopkeeper Platform',
         }
     },
    'BOTTOM OF THE SOUTHEAST STAIRS': {
        'NAME':'BOTTOM OF THE SOUTHEAST STAIRS',
        'DESCRIPTION': 'Theres a jungle to the north.' 
              'There appears to be a tower to the west.',
        'PATHS': {
            'WEST':'FIRST SOUTHEAST TURRENT',
            'NORTH': 'The East Jungle'
        }
    },
   'BOTTOM OF THE NORTHEAST STAIRS': {
        'NAME':'BOTTOM OF THE NORTHEAST STAIRS',
        'DESCRIPTION': 'Theres a jungle to the south.\n' 
              'There appears to be a tower to the west.',
        'PATHS': {
            'WEST':'FIRST NORTHEAST TURRENT',
            'SOUTH': 'The East Jungle'
        }
    },
    'FIRST NORTH TURRENT': {
        'NAME':'NORTHEAST TURRENT',
        'DESCRIPTION': 'The turrent glows purple.\n'
                'You can go south,west,and east.',
        'PATHS': {
            'SOUTH':'The East Jungle',
            'WEST':'SECOND NORTHWEST TURRENT',
            'EAST':'BOTTOM OF NORTHEAST STAIRS'
        }
    },
    'The Northeast Jungle': {
        'NAME':'The East Jungle',
        'DESCRIPTION': 'Brush and vines crawl on the wall.\n'
                'There appears to be a path to the northwest.\n'
                'Theres a path to the south',
        'PATHS': {
            'NORTH':'BOTTOM OF THE NORTH',
            'SOUTH': 'EAST WOLVES CAMP',
            'NORTHWEST': 'THE FIRST NORTHEAST TURRENT'
        }
    },
    'The Southeast Jungle': {
        'NAME':'The West Jungle',
        'DESCRIPTION': 'Brush and vines crawl on the wall.\n'
                    'There appears to be a path to the south.\n'
                    'Theres a path to the norteast.',
        'PATHS': {
            'NORTH': 'WRAITHS CAMP',
            'SOUTH': 'BOTTOM OF THE SOUTH STAIRS',
            'SOUTHWEST': 'THE FIRST SOUTHEAST TURRENT'
        }
    },
    'EAST GOLEM CAMP': {
        'NAME':'EAST GOLEM CAMP',
        'DESCRIPTION': 'You are met by 2 golems,one looking bigger than the other.\n'
                    'There\'s a path to the south.',
        'PATHS': {
            'NORTH': 'THE FIRST NORTHEAST TURRENT',
            'NORTHEAST': ''
        }
    }
}
current_node = world_map['Shopkeeper Platform']
directions = ['NORTH', 'SOUTH', 'NORTHEAST', 'EAST', 'SOUTHEAST', 'WEST', 'SOUTHWEST', 'NORTHWEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_ ')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You cannot go that way')
    else:
        print('command not recognized')
    print()

