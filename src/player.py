# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, item_list):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        # Check if valid room in direction
        if getattr(self.current_room, f'{direction}_to') is not None:
        # if so, update current_room to new room and print desctiption  
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(self.current_room)
        else:
            # Print error message
            print('You cannot go that way.')