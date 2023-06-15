class Object:
    def __init__(self, pos, boxs):
        """
        Create an object with collisions
        pos : (x, y) - The start window position (x and y are floats)
        boxs : [
            (x1_1, y1_1, x2_1, y2_1),
            (x1_2, y1_2, x2_2, y2_2),
            ...
        ] - The list of collision boxs (x and y are floats)
        """
        self.pos = pos
        self.x, self.y = pos
        self.boxs = boxs