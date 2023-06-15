import sys
sys.path.append("..")

from objects.Circle import Circle
import config

class BotObject(Circle):
    def __init__(self, pos):
        """
        Create an bot circle
        pos : (x, y) - The start window position (x and y are floats)
        """
        Circle.__init__(self, pos, config.CIRCLE_RADIUS, config.BOT_COLOR)