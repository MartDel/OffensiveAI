import sys
sys.path.append("..")

from objects.MovingObject import MovingObject
import config

class BotObject(MovingObject):
    def __init__(self, pos, alpha):
        """
        Create an bot circle
        pos : (x, y) - The start window position (x and y are floats)
        alpha : float - The start angle
        """
        MovingObject.__init__(self, pos, alpha, config.BOT_SPEED, config.BOT_COLOR)