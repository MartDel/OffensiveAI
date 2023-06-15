import sys
sys.path.append("..")

from objects.MovingObject import MovingObject
import config

class AIObject(MovingObject):
    def __init__(self, pos, alpha, is_leader = False):
        """
        Create an AI circle
        pos : (x, y) - The start window position (x and y are floats)
        alpha : float - The start angle
        is_leader : bool = False - If the current AI is the group leader
        """
        self.is_leader = is_leader
        MovingObject.__init__(self, pos, alpha, config.AI_SPEED, config.AI_COLOR)