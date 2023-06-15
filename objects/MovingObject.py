import sys, math
sys.path.append("..")

from .Object import Object
import config

class MovingObject(Object):
    def __init__(self, pos, alpha, speed, color, size = 1):
        """
        Create a moving object (triangle)
        pos : (x, y) - The start window position (x and y are floats)
        alpha : float - The start angle
        speed : float - The object speed
        color : (r, g, b) - The shape color (r, g and b are floats)
        size : float - The shape size
        """
        self.alpha = alpha
        self.speed = speed
        self.color = color
        self.size = size

        # Determine the collision box
        box_width = (config.TRIANGLE_LENGTH + 3) * size
        x1, y1 = box_width, box_width
        x2, y2 = box_width, box_width
        box1 = (x1, y1, x2, y2)

        Object.__init__(self, pos, [box1])
    
    def move_forward(self, objects):
        """ Move forward between 2 frames """
        # Determine the destination
        x = self.speed * math.cos(self.alpha) + self.x
        y = self.speed * math.sin(self.alpha) + self.y

        # Check if it's valid (collisions and borders)
        if x < 0 or y < 0 or x > config.WIDTH or y > config.HEIGHT:
            return
        if Object.is_any_conflict(self, objects):
            return

        # Set the nex position
        self.pos = (x, y)
        self.x, self.y = self.pos

    def draw(self, window):
        """ Draw the current object """
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