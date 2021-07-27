from classes.world import World

def initialize():
    global the_world
    the_world = World()
    the_world.load_tiles()