import math

# Window params
WIDTH, HEIGHT = 800, 600
CAPTION = "Simulation"
FPS = 60

# Drawing params
BACKGROUND_COLOR = (0, 0, 0)
BOX_COLOR = (255, 255, 255)
AI_COLOR = (255, 0, 0)
BOT_COLOR = (0, 0, 255)
ALPHA_DELTA = (2 * math.pi) / 3 # The angle between the head and foots
TRIANGLE_LENGTH = 15

# Start params
AI_START_POS = [
    # Leader
    (100, 100),

    # Soldiers
    (100, 50), 
    (50, 100)
]
BOT_START_POS = (50, HEIGHT - 50)
AI_START_ALPHA = 0 # Rad
BOT_START_ALPHA = 0 # Rad
AI_SPEED = 2 # Pixel per frame
BOT_SPEED = 1 # Pixel per frame