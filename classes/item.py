class Item:
    def __init__(self, name, description, value=0):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, value=value)
