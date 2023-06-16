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

        self.is_border = False

        self.ui_boxes = self.get_final_boxes()
        self.coord_boxes = self.get_coord_boxes()

        self.linked_boxes = [] # Objects to ignore
    
    def is_conflict(self, object):
        """ Check if there is a box conflicting with the given object """
        if object in self.linked_boxes:
            return False

        for my_box in self.coord_boxes:
            x1_min, y1_min, x1_max, y1_max = my_box

            for obj_box in object.coord_boxes:
                x2_min, y2_min, x2_max, y2_max = obj_box

                # Check x
                if x1_max < x2_min or x2_max < x1_min:
                    return False
                
                # Check y
                if y1_max < y2_min or y2_max < y1_min:
                    return False

        return True

    def get_final_boxes(self):
        """ Determine the pygame boxes """
        return [
            (
                self.x - box[0],
                self.y - box[1],
                box[0] + box[2],
                box[1] + box[3]
            ) for box in self.boxes
        ]

    def get_coord_boxes(self):
        """ Determine the coord boxes """
        return [
            (
                self.x - box[0],
                self.y - box[1],
                self.x + box[2],
                self.y + box[3],
            ) for box in self.boxes
        ]

    def draw_boxes(self, window, color = config.BOX_COLOR, fill = False):
        """ Draw all current object boxes """
        import pygame

        for box in self.ui_boxes:
            pygame.draw.rect(window, color, box, 2 if not fill else 0)
    
    @staticmethod
    def draw_all_boxes(window, objects):   
        """ Draw all given objects boxes """     
        for obj in objects:
            obj.draw_boxes(window)

    @staticmethod
    def is_any_conflict(obj, objects):
        """ Check if the given obj has conflict with another """
        for o in objects:
            if obj == o:
                continue
            
            if obj.is_conflict(o):
                return o
        
        return None