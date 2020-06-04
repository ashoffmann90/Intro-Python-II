from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Items

items = {
    'staff': Item('Staff', 'Lets you focus your magic.'),
    'potion': Item('Potion', 'Restores health.'),
    'meme': Item('Meme', 'You actually lost the game.'),
    'light': Item('Phial of Galadriel', 'A light to you in dark places.')
}

room['outside'].items.append(items['light'])
room['foyer'].items.append(items['staff'])
room['overlook'].items.append(items['potion'])
room['treasure'].items.append(items['meme'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Drew", room["outside"])

# Write a loop that:
#

while True:
    pInput = input(
        '\nWhat will you do?\n\nTo view controls, enter c: \n\n')
    player_input = pInput.lower().split(' ')

    if len(player_input) == 1:
        if pInput == 'n' or pInput == 's' or pInput == 'e' or pInput == 'w':
            player.move(pInput)
            print(
                f'\n{player.name} is in the {player.current_room.name}\n{player.current_room.description}\n')
        elif pInput == 'q':
            print('You have exited the game.')
            break
        elif pInput == 'f':
            player.current_room.search()
        elif pInput == 'i':
            player.show_inventory()
        elif pInput == 'c':
            player.show_controls()
    elif len(player_input) == 2:
        if player_input[0] in ['get', 'take']:
            if items[player_input[1]]:
                player.add_to_inventory(items[player_input[1]])
                print(f"You've picked up an item.")
            else:
                print(f'There is no item named {player_input[1]}')
        elif player_input[0] == 'drop':
            if items[player_input[1]]:
                player.drop_item(items[player_input[1]])
                print('You dropped an item.')
            else:
                print(f'There is no item named {player_input[1]}')
        else:
            print('Not a valid command')
    else:
        print('Not a valid command.')

# LONG WAY, NOT DRY, MUST REMOVE DEF MOVE METHOD IN PLAYER.PY IF USING THIS WAY
# while True:
#     direction = input("Where are you going n, e, s, w?")
#     if direction == "n":
#         if player.current_room.n_to == None:
#             print('There is nothing in that direction!')
#             continue
#         player.current_room = player.current_room.n_to
#     elif direction == "e":
#         if player.current_room.e_to == None:
#             print('There is nothing in that direction!')
#             continue
#         player.current_room = player.current_room.e_to
#     elif direction == "s":
#         if player.current_room.s_to == None:
#             print('There is nothing in that direction!')
#             continue
#         player.current_room = player.current_room.s_to
#     elif direction == "w":
#         if player.current_room.w_to == None:
#             print('There is nothing in that direction!')
#             continue
#         player.current_room = player.current_room.w_to
#     elif direction == 'q':
#         print("You've exited the game.")
#         break
#     print(player.current_room)
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
