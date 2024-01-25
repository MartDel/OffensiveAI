import sys, math
sys.path.append("..")

from objects.Object import Object
from utils.Utils import Utils
from utils.Ray import Ray
import config

class MovingObject(Object):
    def __init__(self, pos, alpha, speed, color, size = 1, is_static = False):
        """
        Create a moving object (triangle)
        pos : (x, y) - The start window position (x and y are floats)
        alpha : float - The start angle
        speed : float - The object speed
        color : (r, g, b) - The shape color (r, g and b are floats)
        size : float = 1 - The shape size
        is_static : bool = False - If the AI should stay static (no movements)
        """
        self.alpha = alpha
        self.speed = speed
        self.color = color
        self.size = size
        self.is_static = is_static
        self.rays = []

        # Determine the collision box
        box_width = (config.TRIANGLE_LENGTH + 3) * size
        x1, y1 = box_width, box_width
        x2, y2 = box_width, box_width
        box1 = (x1, y1, x2, y2)

        Object.__init__(self, pos, [box1])
            
    def move_forward(self, objects, raycast = True):
        """ Move forward between 2 frames """
        if self.is_static:
            return

        # Determine the destination
        x = self.speed * math.cos(self.alpha) + self.x
        y = self.speed * math.sin(self.alpha) + self.y

        # Check if it's valid (collisions and borders)
        objects = self.filter_objects(objects)
        if Object.is_any_conflict(self, objects) != None:
            return

        # Set the new position
        self.pos = (x, y)
        self.x, self.y = self.pos
        self.ui_boxes = self.get_final_boxes()
        self.coord_boxes = self.get_coord_boxes()

        # Update the raycaster
        if raycast:
            self.raycast(objects)
    
    def look_for(self, target, objects, raycast = False):
        """ Move to the given position """
        self.alpha = Utils.get_alpha_to(target, self.pos)
        
        # Update the raycaster
        if raycast:
            self.raycast(objects)
    
    def raycast(self, objects, range = config.RAYCASTER_RANGE, step = config.RAYCASTER_STEP, distance = config.RAY_DISTANCE):
        """ Update the raycaster """
        self.rays = []
        a = self.alpha - range
        stop = self.alpha + range
        while a <= stop:
            self.rays.append(Ray(self.pos, a, distance))
            a += step
        
        # Get objects that the object is able to see
        self.targets = [ ray.cast(self, objects, self.filter_objects) for ray in self.rays ]

    def filter_objects(self, objects, pos=None):
        """ Work with less objects """
        pos = pos if pos is not None else self.pos
        objs = filter(lambda obj: obj.is_border or ((obj.x - pos[0]) ** 2) + ((obj.y - pos[1]) ** 2) <= config.MAX_LOAD_RANGE ** 2, objects)
        return list(objs)

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
            
    def draw_rays(self, window):
        """ Draw rays of raycaster """
        # import pygame

        for ray in self.rays:
            ray.draw(window)
        
        # pygame.draw.circle(window, (255, 0, 0), self.pos, config.MAX_LOAD_RANGE, 2)