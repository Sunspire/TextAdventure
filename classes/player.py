class player():
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp
        self.x = 0
        self.y = 0
    
    def __str__(self):
        return "{}, {}".format(self.name, self.hp)

    def move(self, lx, ly, world):
        if world.tile_exists((self.x + lx, self.y + ly)):
            self.x += lx
            self.y += ly
        else:
            print('you cannot move there')        

    def move_north(self, world):
        self.move(lx=0, ly=-1, world=world)

    def move_south(self, world):
        self.move(lx=0, ly=1, world=world)

    def move_east(self, world):
        self.move(lx=1, ly=0, world=world)

    def move_west(self, world):
        self.move(lx=-1, ly=0, world=world)

    def do_action(self, action, world):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(world)