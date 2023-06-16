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