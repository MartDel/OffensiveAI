import sys
from math import pi
sys.path.append("..")

from objects.MovingObject import MovingObject
from objects.BotObject import BotObject
from objects.Object import Object
from utils.Utils import Utils
from utils.Ray import Ray
import config

class AIObject(MovingObject):
    def __init__(self, pos, alpha):
        """
        Create an AI circle
        pos : (x, y) - The start window position (x and y are floats)
        alpha : float - The start angle
        is_leader : bool = False - If the current AI is the group leader
        """
        MovingObject.__init__(self, pos, alpha, config.AI_SPEED, config.AI_COLOR)
    
    def pathfinder(self, dest_obj, objects, simu):
        """ Try to reach the destination by dodging the wall """
        # Start by casting a ray
        ray_alpha = Utils.get_alpha_to(dest_obj.pos, self.pos)
        ray_distance = Utils.distance_between(self.pos, dest_obj.pos)
        ray_filter = lambda objs, pos : list(filter(lambda obj: not isinstance(obj, BotObject), self.filter_objects(objs, pos)))
        ray = Ray(self.pos, ray_alpha, ray_distance)
        cast_result = ray.cast(self, objects, ray_filter)
        ray.draw(simu.window)
        self.raycast(objects, range = pi, step = pi / 4, distance = 20) # Check around not to collide
        if cast_result is None and all(target is None for target in self.targets):
            return dest_obj.pos

        # Init the pathfinder
        box = self.boxes[0]
        distance_coef = 2.1
        neighbors = [(-box[0] * distance_coef, 0), (0, -box[1] * distance_coef), (box[2] * distance_coef, 0), (0, box[3] * distance_coef)]

        def is_already_checked(layers, pos):
            for layer in layers[::-1]: # Loop the layers list after reversing it
                for obj in layer:
                    if obj.pos == pos:
                        return True
            return False

        found = False
        layers = [[self]] # Discovered spaces (box)
        while len(layers[-1]) > 0 and not found:
            new_layer = []
            for obj in layers[-1]: # Loop through the previous layer
                for n in neighbors: # Check each neighors of the current layer box
                    # Define the working box (with an Object instance)
                    new_pos = (obj.x + n[0], obj.y + n[1])
                    if is_already_checked(layers, new_pos):
                        continue
                    new_obj = Object(new_pos, self.boxes)

                    # Check collisions
                    touched = Object.is_any_conflict(new_obj, self.filter_objects(objects, new_pos))
                    if touched is None:
                        new_layer.append(new_obj)
                    else:
                        if touched == dest_obj:
                            found = True
            
            layers.append(new_layer)
        
        if not found:
            return None
        
        import pygame

        # Determine the new direction
        next_point = dest_obj.pos # Starting from the new destination
        i = len(layers) - 1
        while i > 0:
            layers[i].sort(key=lambda obj: Utils.distance_between(obj.pos, next_point))
            next_point = layers[i][0].pos
            pygame.draw.circle(simu.window, (255, 0, 0), next_point, 2)
            i -= 1
        
        return next_point