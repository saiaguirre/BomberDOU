class Blocks():
    """ 'Blocks' is an abstract class made so all types of blocks can share
    basic features: position and size, mostly. They are all 'alive' while on
    screen."""
    def __init__(self):
        self.can_be_broken: None


class B_unbreakable(Blocks):
    """ This kind of blocks are impossible to break and they are created to
    form the grid that conforms the map, giving the game 1x17 corridors, for
    both rows and columns."""
    def __init__(self):
        self.live = True
        self.life = 100


class B_breakable(Blocks):
    """ This blocks will be obstacles on the corridors the player will have to
    walk on. These can be destroyed only with bombs."""
    def die(self):
        self.live = False
