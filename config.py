from math import pi

# Window params
WIDTH, HEIGHT = 800, 600
CAPTION = "Simulation"
FPS = 30

# Drawing params
BACKGROUND_COLOR = (0, 0, 0)
BOX_COLOR = (255, 255, 255)
AI_COLOR = (255, 0, 0)
BOT_COLOR = (0, 0, 255)
ALPHA_DELTA = (2 * pi) / 3 # The angle between the head and foots
TRIANGLE_LENGTH = 15
WIN_RECT_COLOR = (0, 255, 0)
RAY_COLOR = (0, 255, 0)
RAY_WIDTH = 3
RAY_BOX_COLOR = (255, 0, 0)
WALL_COLOR = (160, 160, 160)

# Start params
AI_START_POS = [
    (100, 100),
    # (100, 50), 
    # (50, 100)
]
BOT_START_POS = (50, HEIGHT - 50)
AI_START_ALPHA = pi/4 # Rad
BOT_START_ALPHA = -pi / 5  # Rad
AI_SPEED = 1.5 # Pixel per frame
BOT_SPEED = 1 # Pixel per frame


# Win condition
WIN_RECT_WIDTH = 100
WIN_RECT_HEIGHT = 100

# Raycaster
RAY_START_LENGTH = 1
RAY_INC = 1 # Raycaster accuracy
RAY_BOX_SIZE = 5
RAY_DISTANCE = 100
RAYCASTER_RANGE = pi / 4 # Rad
RAYCASTER_STEP = pi / 15 # Rad
MAX_LOAD_RANGE = RAY_DISTANCE + 20

# Walls
WALL_WIDTH = 40
WALL_HEIGHT = 20
# WALLS_COORD = [(100, 425), (100, 350), (100, 275), (100, 200), (175, 500), (175, 350), (175, 275), (175, 200), (175, 125), (250, 500), (250, 275), (250, 200), (250, 125), (250, 50), (325, 500), (325, 425), (325, 200), (325, 125), (325, 50), (400, 500), (400, 425), (400, 350), (400, 125), (400, 50), (475, 500), (475, 425), (475, 350), (475, 275), (475, 50), (550, 500), (550, 425), (550, 350), (550, 275)]
WALLS_COORD = [(100, 425), (100, 350), (100, 200), (175, 500), (175, 200), (175, 125), (250, 275), (250, 125), (325, 425), (325, 125), (325, 50), (400, 500), (400, 350), (475, 500), (475, 50), (550, 425), (550, 275)]

# Algo
MIN_PATHFINDER = 100