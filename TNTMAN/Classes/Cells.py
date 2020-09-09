class Cells():
    """ Cells are the minimum part in which the map is divided. These
    create a grid used by the Map."""
    def __init__(self, pos, content):
        self.size = (32, 32)  # Pixel size.
        self.content = content  # Defines what other class will ocupy a cell.
        self.position = []  # Defines the abstract position [x, y] of the cell.
        self.position = pos
