import sys
sys.path.append("..")

from objects.Circle import Circle
import config

class AIObject(Circle):
    def __init__(self, pos, is_leader = False):
        """
        Create an AI circle
        pos : (x, y) - The start window position (x and y are floats)
        is_leader : bool = False - If the current AI is the group leader
        """
        self.is_leader = is_leader
        Circle.__init__(self, pos, config.CIRCLE_RADIUS, config.AI_COLOR)