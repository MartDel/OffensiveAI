import pygame, os

from objects.AIObject import AIObject
import config

# ----------------------------- Simulation class ----------------------------- #

class Simulation:
    def __init__(self, w = config.WIDTH, h = config.HEIGHT, caption = config.CAPTION):
        self.width, self.height = w, h
        self.caption = caption

        # Init AI objects
        self.AI_objects = [ AIObject(pos) for pos in config.AI_START_POS ]
        self.AI_objects[0].is_leader = True # The first one is the leader

    def trigger_event(self, event):
        """ Trigger all pygame event """
        if event.type == pygame.QUIT:
            self.game_running = False
    
    def draw_window(self):
        """ Draw all the window each tick """
        self.window.fill(config.BACKGROUND_COLOR) # Window background

        # Draw AI circles
        for ai in self.AI_objects:
            ai.draw(self.window)
        
        # Draw the bot circle (victim)
        pygame.draw.circle(self.window, config.BOT_COLOR, config.BOT_START_POS, config.CIRCLE_RADIUS)
    
    def run_UI(self):
        # Init PyGame
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

        # Main loop
        self.game_running = True
        self.clock = pygame.time.Clock()
        while self.game_running:
            # Event loop
            for event in pygame.event.get():
                self.trigger_event(event)

            # Draw the window content
            self.draw_window()
        
            # Update diplay
            pygame.display.update()
            self.clock.tick(config.FPS) # How many refresh per second

        # Exiting
        pygame.display.quit()
    
    def force_quit(self):
        """ Exiting by killing the python process """
        os.kill(os.getpid(), 9)

# ---------------------------------- Testing --------------------------------- #

if __name__ == "__main__":
    simu = Simulation()
    simu.run_UI()
    simu.force_quit()