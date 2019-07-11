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

# Main
#

# Create Items

broadsword = Item('Broadsword', 'A standard broadsword, forged in steel')
axe = Item('Axe', 'A standard tree-felling axe.')
pitchfork = Item('Pitchfork', 'A standard pitchfork, engraved "Farmer Joe"')

# Item dictionary

items = {
    ''
}

# Add items to rooms

room['foyer'].items.extend([broadsword, axe, pitchfork])

# Make a new player object that is currently in the 'outside' room.

new_player = Player('Mario', room['outside'], None)

valid_directions = ['n', 's', 'e', 'w']

# # Write a loop that:
while True:

# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
    # ^^printing of name and desctiption abstracted to Room class

# # * Waits for user input and decides what to do.
    direction = input('Which direction would you like to go?\n [n] North [s] South [e] East [w] West    [q] Quit\n')

    if len(direction) == 1:

    # # If the user enters a cardinal direction, attempt to move to the room there.
        if direction in valid_directions:
            new_player.move(direction)

    # # If the user enters "q", quit the game.
        elif direction is 'q':
            print('Goodbye!')
            break

    # Print player inventory
        elif direction is 'i':
            new_player.print_inventory()

        else:
            print('That is an invalid direction.')

    else:
        verb = ' '.join(direction.split(' ')[0:1])
        item = direction.split(' ')[-1]
        noun = item.capitalize()

    # Item dictionary

        items = {
            'broadsword': broadsword,
            'axe': axe,
            'pitchfork': pitchfork
        }
    
    # Pick up items
        if verb == 'get':
            if [item.name == {noun} for item in new_player.current_room.items]:
                new_player.get_item(items[item])
            else:
                print(f'There is no {noun} here!')

    # Drop items
        elif verb == 'drop':
            new_player.drop_item(items[item])

    # # Print an error message if the movement isn't allowed.
        else:
            print('I do not understand this command')