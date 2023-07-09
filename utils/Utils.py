import sys, math
sys.path.append("..")

import config

class Utils:
    @staticmethod
    def distance_between(p1, p2):
        """ Get euclidian distance between p1 and p2 """
        return math.sqrt(((float(p1[0]) - float(p2[0])) ** 2) + ((float(p1[1]) - float(p2[1])) ** 2))

    @staticmethod
    def check_border(point):
        """ Check if point is not reaching out borders """
        x, y = point
        return not (x < 0 or y < 0 or x > config.WIDTH or y > config.HEIGHT)
    
    @staticmethod
    def get_alpha_to(dest, pos):
        """ Get the alpha to turn to reach the 'dest' point from the 'pos' point """
        x_delta = abs(float(pos[0] - dest[0]))
        y_delta = abs(float(pos[1] - dest[1]))

        if (dest[0] < pos[0] and dest[1] <= pos[1]):
            # pi <= alpha < 3pi/2
            return math.atan(y_delta / x_delta) + math.pi
        elif (dest[0] >= pos[0] and dest[1] < pos[1]):
            # 3pi/2 <= alpha < 2pi
            return math.atan(x_delta / y_delta) + ((3 * math.pi) / 2)
        elif (dest[0] > pos[0] and dest[1] >= pos[1]):
            # 0 <= alpha < pi/2
            return math.atan(y_delta / x_delta)
        elif (dest[0] <= pos[0] and dest[1] > pos[1]):
            # pi/2 <= alpha < pi
            return math.atan(x_delta / y_delta) + (math.pi / 2)
    
        raise "Alpha error"