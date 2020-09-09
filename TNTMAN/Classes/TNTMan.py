import View  # Import 'View.py' file.
import Entity  # Import 'Entity.py' file.


class TNTMan(Entity.Entity):
    """TNTMan is the playable character. It is designed to move when
       the player wants it to move, and to do it cell by cell."""
    def __init__(self, pos=[1, 1]):
        self.actual_pos = pos
        self.bomb_deployed = False

    def get_bomb_deployed(self):
        return self.bomb_deployed

    def deploy_bomb(self):
        self.bomb_deployed = True

    def move_to(self, direction, is_valid):
        """Called by the Map to make the character move."""
        self.actual_pos[0] = self.actual_pos[0] + direction[0]
        self.actual_pos[1] = self.actual_pos[1] + direction[1]

    def get_new_possible_position(self, direction):
        """ This method allows to calculate which the next possible
            cell could be."""
        aux_list = [1, 1]
        aux_list[0] = self.actual_pos[0] + direction[0]
        aux_list[1] = self.actual_pos[1] + direction[1]
        return aux_list

    def get_position(self):  # Getter
        return self.actual_pos

    def hi_luna_v2(self):
        self.hi_luna()
