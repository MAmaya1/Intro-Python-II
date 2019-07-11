from room import Room
from player import Player

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

# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player('Mario', room['outside'], None)
print(f'Welcome, {new_player.name}!')

# # Write a loop that:
# #
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.

valid_directions = ['n', 's', 'e', 'w']

while True:
    print('\n----------------------------------------------')
    print(f'\nCurrent location: {new_player.current_room.name}')
    print(new_player.current_room.description)
    print(f'\nWhich direction would you like to go?')

    # User input

    direction = input('[n] North [s] South [e] East [w] West    [q] Quit\n')

    if direction in valid_directions:
        new_player.move(direction)
    
    elif direction is 'q':
        print('Goodbye!')
        break
    
    else:
        print('I do not understand that command.')


# #
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.
