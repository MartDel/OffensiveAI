import sys
sys.path.append("..")

from objects.Object import Object
import config

class Wall(Object):
    def __init__(self, pos, width, height, color = config.WALL_COLOR):
        """
        Create a moving object (triangle)
        pos : (x, y) - The start window position (x and y are floats)
        width : float - The wall width
        height : float - The wall height
        """
        self.width = width
        self.height = height
        self.color = color

        # Determine the hitbox
        x1, y1 = 0, 0
        x2, y2 = width, height
        box1 = (x1, y1, x2, y2)

        Object.__init__(self, pos, [box1])
    
    def draw(self, window):
        """ Draw the wall to the screen """
        import pygame
        
        for rect in self.get_final_boxes():
            pygame.draw.rect(window, self.color, rect, 0)