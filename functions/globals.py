from classes.world import World

def init():
    global the_world
    the_world = World()
    the_world.load_tiles()