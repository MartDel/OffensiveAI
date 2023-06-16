from math import pi

# Window params
WIDTH, HEIGHT = 800, 600
CAPTION = "Simulation"
FPS = 60

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
    (100, 50), 
    (50, 100)
]
BOT_START_POS = (50, HEIGHT - 50)
AI_START_ALPHA = pi/4 # Rad
BOT_START_ALPHA = -pi / 5  # Rad
AI_SPEED = 1.5 # Pixel per frame
BOT_SPEED = 1 # Pixel per frame
BOT_RAY_DISTANCE = 100

# Win condition
WIN_RECT_WIDTH = 100
WIN_RECT_HEIGHT = 100

# Raycaster
RAY_START_LENGTH = 1
RAY_INC = 1 # Raycaster accuracy
RAY_BOX_SIZE = 5
RAYCASTER_RANGE = pi / 4 # Rad
RAYCASTER_STEP = pi / 15 # Rad