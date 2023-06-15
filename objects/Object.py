import sys
sys.path.append("..")

import config

class Object:
    def __init__(self, pos, boxes):
        """
        Create an object with collisions
        pos : (x, y) - The start window position (x and y are floats)
        boxes : [
            (x1_1, y1_1, x2_1, y2_1),
            (x1_2, y1_2, x2_2, y2_2),
            ...
        ] - The list of collision boxes (x and y are floats)
        """
        self.pos = pos
        self.x, self.y = pos
        self.boxes = boxes

    def get_final_boxes(self):
        return [
            (
                self.x - box[0],
                self.y - box[1],
                box[2] * 2,
                box[3] * 2
            ) for box in self.boxes
        ]

    def draw_boxes(self, window):
        import pygame

        for box in self.get_final_boxes():
            pygame.draw.rect(window, config.BOX_COLOR, box, 2)
    
    @staticmethod
    def draw_all_boxes(window, objects):        
        for obj in objects:
            obj.draw_boxes(window)