import sys, math
sys.path.append("..")

from objects.MovingObject import MovingObject
import config

class BotObject(MovingObject):
    def __init__(self, pos, alpha, is_static=False):
        """
        Create an bot circle
        pos : (x, y) - The start window position (x and y are floats)
        alpha : float - The start angle
        is_static : bool = False - If the bot should stay static (no movements)
        """
        MovingObject.__init__(self, pos, alpha, config.BOT_SPEED, config.BOT_COLOR, is_static=is_static)