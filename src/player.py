# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f'Name: {self.name}, Room: {self.current_room}'

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("There is nothing in that Direction!")

    def show_inventory(self):
        if not self.items:
            print('You are not carrying anything.')
        else:
            print('Inventory: ')
            for i in self.items:
                print(i.name)

    def add_to_inventory(self, item):
        if len(self.current_room.items) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.pickup_item()
            print('You picked up an item.')
        else:
            print(f'There are no items in this room.')

    def drop_item(self, item):
        if len(self.items) > 0:
            self.items.remove(item)
            self.current_room.items.append(item)
            print('You dropped an item.')
            item.drop_item()

    def show_controls(self):
        print('Movement: \n n for north, \n s for south, \n e for east, \n w for west\nInteract: \n f to search a room, \n get or take to pick up an item, \n drop to drop an item, \n i to view your inventory, \n q to quit the game\n')
