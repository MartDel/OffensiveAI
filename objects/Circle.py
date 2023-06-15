import pygame

from .Object import Object

class Circle(Object):
    def __init__(self, pos, radius, color):
        """
        Create a circle
        pos : (x, y) - The start window position (x and y are floats)
        radius : float - The circle radius
        color : (r, g, b) - The circle color (r, g and b are floats)
        """
        self.radius = radius
        self.color = color

        # Determine the collision box
        x, y = pos
        x1, y1 = x + radius, y + radius
        x2, y2 = x - radius, y - radius
        box1 = (x1, y1, x2, y2)

        Object.__init__(self, pos, [box1])
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, self.pos, self.radius)
