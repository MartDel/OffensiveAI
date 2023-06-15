import sys
sys.path.append("..")

from objects.MovingObject import MovingObject
import config

class BotObject(MovingObject):
    def __init__(self, pos):
        """
        Create an bot circle
        pos : (x, y) - The start window position (x and y are floats)
        """
        MovingObject.__init__(self, pos, 0, config.BOT_COLOR)