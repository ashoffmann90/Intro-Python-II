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

    def print_items(self):
        if not self.items:
            print('You are not carrying anything.')
        else:
            print('Inventory: ')
            for i in self.items:
                print(i.name)

    def grab_item(self, item):
        if len(self.current_room.items) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            print('You picked up {}')
        else:
            print(f'There are no items in this room.')

    def drop_item(self, item):
        if len(self.items) > 0:
            self.items.remove(item)
            self.current_room.items.append(item)
            item.drop()
