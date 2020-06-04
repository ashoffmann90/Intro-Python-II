class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup_item(self):
        print(f'Picked up: \n{self.name}')

    def drop_item(self):
        print(f'Dropped: \n{self.name}')
