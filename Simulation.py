import pygame, os

from objects.AIObject import AIObject
from objects.BotObject import BotObject
from objects.MovingObject import MovingObject
from objects.Wall import Wall
from objects.Object import Object
import config

# ----------------------------- Simulation class ----------------------------- #

class Simulation:
    def __init__(self, w = config.WIDTH, h = config.HEIGHT, caption = config.CAPTION, is_static = False):
        """
        Create a simulation with a 'player' (BotObject) and 'ennemies' (AIObject)
        w : int - The window width
        h : int - The window height
        caption : str - The window title
        is_static : bool - If the simulation should stay static (no movements from bot or AIs)
        """
        self.width, self.height = w, h
        self.caption = caption
        self.objects = []
        self.is_static = is_static

        # Init borders
        self.objects.append(Wall((0, 0), 10, config.HEIGHT))
        self.objects.append(Wall((0, 0), config.WIDTH, 10))
        self.objects.append(Wall((config.WIDTH - 10, 0), 10, config.HEIGHT))
        self.objects.append(Wall((0, config.HEIGHT - 10), config.WIDTH, 10))
        for obj_idx in range(4):
            self.objects[obj_idx].is_border = True

        # Add obstacles
        self.objects += [ Wall(pos, config.WALL_WIDTH, config.WALL_HEIGHT) for pos in config.WALLS_COORD ]

        # Init AI objects
        self.AI_objects = [ AIObject(pos, config.AI_START_ALPHA, is_static=self.is_static) for pos in config.AI_START_POS ]
        self.objects += self.AI_objects

        # Init the bot (victim)
        self.victim = BotObject(config.BOT_START_POS, config.BOT_START_ALPHA, is_static=self.is_static)
        # self.victim = BotObject((400, 300), config.BOT_START_ALPHA)
        self.objects.append(self.victim)
    
    def frame_action(self):
        """ What to do at each frame """
        if self.first_frame:
            pass

        # Move all objects
        for obj in filter(lambda obj: isinstance(obj, MovingObject), self.objects):
            if isinstance(obj, AIObject): 
                new_destination = obj.pathfinder(self.victim, self.objects, self)
                obj.look_for(new_destination, self.objects)
            obj.move_forward(self.objects, raycast=isinstance(obj, BotObject))

        # Win condition
        if self.victim.x >= config.WIDTH - config.WIN_RECT_WIDTH and self.victim.y <= config.WIN_RECT_HEIGHT:
            self.exit()

    def init(self):
        """ Init PyGame """
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

        self.game_running = True
        self.boxes_printed = False
        self.rays_printed = False
        self.pause = self.is_static
    
        self.first_frame = True

        self.clock = pygame.time.Clock()

        self.victim.look_for((config.WIDTH, 0), self.objects)

    def trigger_event(self, event):
        """ Trigger all pygame event """
        if event.type == pygame.QUIT:
            self.exit() # Exiting
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.exit() # Exiting
            elif event.key == pygame.K_SPACE:
                self.boxes_printed = not self.boxes_printed # Debug collisions
                self.rays_printed = not self.rays_printed # Debug collisions
            elif event.key == pygame.K_p:
                self.pause = not self.pause # Make pause or resume
    
    def draw_window(self):
        """ Draw all the window each tick """
        self.window.fill(config.BACKGROUND_COLOR) # Window background

        # Win rect
        pygame.draw.rect(self.window, config.WIN_RECT_COLOR, (config.WIDTH - config.WIN_RECT_WIDTH, 0, config.WIN_RECT_WIDTH, config.WIN_RECT_HEIGHT), 2)

        # Draw objects
        for obj in self.objects:
            obj.draw(self.window)

        # Draw collisions
        if self.boxes_printed:
            Object.draw_all_boxes(self.window, self.objects)

        # Draw rays
        if self.rays_printed:
            for obj in self.objects:
                if not isinstance(obj, MovingObject):
                    continue
                obj.draw_rays(self.window)
        
    
    def run_UI(self):
        """ Run the simu with UI """
        self.init()

        # Main loop
        while self.game_running:
            # Event loop
            for event in pygame.event.get():
                self.trigger_event(event)

            # Draw the window content
            self.draw_window()

            # Do some calculs, movements
            if not self.pause:
                self.frame_action()
        
            # Update diplay
            pygame.display.update()
            self.clock.tick(config.FPS) # How many refresh per second

            self.first_frame = False

        # Exiting
        pygame.display.quit()

    def exit(self):
        """ Tell the simulation to stop """
        self.game_running = False
    
    def force_quit(self):
        """ Exiting by killing the python process """
        os.kill(os.getpid(), 9)

# ---------------------------------- Testing --------------------------------- #

if __name__ == "__main__":
    simu = Simulation(is_static=True)
    simu.run_UI()
    simu.force_quit()