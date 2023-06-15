import sys, math
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
    
    def look_for(self, target):
        """ Move to the given position """
        x_delta = abs(float(self.x - target[0]))
        y_delta = abs(float(self.y - target[1]))

        if (target[0] < self.x and target[1] <= self.y):
            # pi <= alpha < 3pi/2
            self.alpha = math.atan(y_delta / x_delta) + math.pi
        elif (target[0] >= self.x and target[1] < self.y):
            # 3pi/2 <= alpha < 2pi
            self.alpha = math.atan(x_delta / y_delta) + ((3 * math.pi) / 2)
        elif (target[0] > self.x and target[1] >= self.y):
            # 0 <= alpha < pi/2
            self.alpha = math.atan(y_delta / x_delta)
        elif (target[0] <= self.x and target[1] > self.y):
            # pi/2 <= alpha < pi
            self.alpha = math.atan(x_delta / y_delta) + (math.pi / 2)