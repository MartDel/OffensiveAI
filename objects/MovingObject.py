import sys, math
sys.path.append("..")

from .Object import Object
import config

class MovingObject(Object):
    def __init__(self, pos, alpha, color, size = 1):
        """
        Create a moving object (triangle)
        pos : (x, y) - The start window position (x and y are floats)
        alpha : float - The start angle
        color : (r, g, b) - The shape color (r, g and b are floats)
        size : float - The shape size
        """
        self.alpha = alpha
        self.color = color
        self.size = size

        # Determine the collision box
        box_width = (config.TRIANGLE_LENGTH + 3) * size
        x1, y1 = box_width, box_width
        x2, y2 = box_width, box_width
        box1 = (x1, y1, x2, y2)

        Object.__init__(self, pos, [box1])

    def draw(self, window):
        import pygame

        def getPosByAlpha(alpha):
            """ Determine coord with the angle """
            x = self.size * config.TRIANGLE_LENGTH * math.cos(alpha) + self.x
            y = self.size * config.TRIANGLE_LENGTH * math.sin(alpha) + self.y
            return x, y

        points = [
            getPosByAlpha(self.alpha),
            getPosByAlpha(self.alpha + config.ALPHA_DELTA),
            self.pos,
            getPosByAlpha(self.alpha - config.ALPHA_DELTA)
        ]
        pygame.draw.polygon(window, self.color, points)