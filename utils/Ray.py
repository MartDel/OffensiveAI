import sys, math
sys.path.append("..")

import config
from objects.Object import Object

class Ray:
    def __init__(self, start, alpha, max_distance):
        """
        Create a casting ray, to search for a collision box
        start : (x, y) - The ray first point (x and y are floats)
        alpha : float - The ray angle
        max_distance : float - The ray max length
        """
        self.start_point = self.end_point = start
        self.alpha = alpha
        self.max_distance = max_distance
        self.hitbox = None
    
    def cast(self, origin, all_objects, filter):
        """ Send the ray from the 'origin' object and returns the hit box """
        self.hit = None
        self.length = config.RAY_START_LENGTH
        while self.length <= self.max_distance and self.hit == None:
            # Determine end point
            self.end_point = self.length * math.cos(self.alpha) + self.start_point[0], self.length * math.sin(self.alpha) + self.start_point[1]

            # Check the collision
            self.create_box(origin)
            self.hit = Object.is_any_conflict(self.hitbox, filter(all_objects, self.end_point))

            # Increase the ray length
            self.length += config.RAY_INC

        return self.hit

    def create_box(self, origin):
        """ Generate the hitbox of the ray end point """
        x1, y1 = config.RAY_BOX_SIZE, config.RAY_BOX_SIZE
        x2, y2 = config.RAY_BOX_SIZE, config.RAY_BOX_SIZE
        box1 = (x1, y1, x2, y2)

        # Create the object for the box
        self.hitbox = Object(self.end_point, [box1])
        self.hitbox.linked_boxes.append(origin)
    
    def draw(self, window):
        """ Draw the draw to the screen """
        if self.hitbox is None:
            return
        
        import pygame

        # Draw the line
        pygame.draw.line(window, config.RAY_COLOR, self.start_point, self.end_point, config.RAY_WIDTH)

        # Draw the box
        self.hitbox.draw_boxes(window, color = config.RAY_BOX_COLOR, fill = True)