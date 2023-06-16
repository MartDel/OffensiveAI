import sys, math
sys.path.append("..")

from objects.Object import Object
from utils.Utils import Utils
from utils.Ray import Ray
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
        self.rays = []

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
        objects = self.filter_objects(objects)
        if Object.is_any_conflict(self, objects) != None:
            return

        # Set the new position
        self.pos = (x, y)
        self.x, self.y = self.pos
        self.ui_boxes = self.get_final_boxes()
        self.coord_boxes = self.get_coord_boxes()

        # Update the raycaster
        self.raycast(objects)
    
    def look_for(self, target, objects):
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
        
        # Update the raycaster
        objects = self.filter_objects(objects)
        self.raycast(objects)
    
    def raycast(self, objects):
        """ Update the raycaster """
        self.rays = []
        a = self.alpha - config.RAYCASTER_RANGE
        stop = self.alpha + config.RAYCASTER_RANGE
        step = config.RAYCASTER_STEP
        while a <= stop:
            self.rays.append(Ray(self.pos, a, config.RAY_DISTANCE))
            a += step
        
        # Get objects that the object is able to see
        self.targets = [ ray.cast(self, objects) for ray in self.rays ]

    def filter_objects(self, objects):
        """ Work with less objects """
        objs = filter(lambda obj: obj.is_border or ((obj.x - self.x) ** 2) + ((obj.y - self.y) ** 2) <= config.MAX_LOAD_RANGE ** 2, objects)
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