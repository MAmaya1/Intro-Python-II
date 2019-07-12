# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, item_list):
        self.name = name
        self.current_room = current_room
        self.items = []

    # Move Player

    def move(self, direction):
        # Check if valid room in direction
        if getattr(self.current_room, f'{direction}_to') is not None:
        # if so, update current_room to new room and print desctiption  
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(self.current_room)
        else:
            # Print error message
            print('You cannot go that way.')

    # Print Item Inventory

    def print_inventory(self):
        if len(self.items) > 0:
            print('You are carrying:\n' + ', '.join([item.name for item in self.items]))
        else:
            print('You are not carrying any items')

    # Pick Up Item

    def get_item(self, item): 
        if not item in self.items:
            if len(self.items) < 2:
                self.items.append(item)
                print(f'You have picked up {item.name}')
            else:
                print('You can only carry a maximum of 2 items at this point.')
        else:
            print('You can only carry one item of this type')

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f'You have dropped {item.name}')
        else:
            print('This item does not exist in your inventory.')