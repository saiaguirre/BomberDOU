import os       # Import sys and os for python to understand the local
import sys      # directory.
import Map      # Import File 'Map.py'.
import pygame   # Import pygame module.
import View     # Import 'View.py' module.
import threading
from pydispatch import dispatcher
import time
sys.path.append(os.path.dirname(__file__))
Thread_señal = 'Thread_señal' 
Thread_sender = 'Thread_sender'

CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}
""" If any of these arrows are pressed, this dictionary searches for a
 list, which represents x and y values for TNTMan movement """


class Thread(threading.Thread):
    def __init__(self, time_bomb):
        super().__init__()
        self.time_explode = time_bomb
    def run(self):
        time.sleep(self.time_explode)
        dispatcher.send(message = 'Listo', signal=Thread_señal, sender=Thread_sender)


class Driver:

    """ Driver is the link between Map (the game controller) and the
        View, allowing to represent what happens on the game visually."""

    def __init__(self):
        self.thread = None
        self.dimentions = (800, 600)  # Defines pixel dimentions of the game.
        # self.clock = pygame.time.Clock()
        # self.bombtime = 0
        self.map = Map.Map(self.dimentions)  # Creates map.
        self.map.build_map_array()  # Creates a cell array for segmenting the
        # map.
        self.view = View.View(self.dimentions, self.map)  # Creates View.
        self.view.load_blocks()  # Load blocks images.
        self.main_loop()  # Calls the main loop.

    def thread_finished(self, message):
        print('UWU')
        self.map.explode_bomb()

    def main_loop(self):
        """ Main loop keeps looping over and over as long as the game
            lasts, so everything that needs to be constantly checked
            works"""

        while True:
            # self.clock.tick()
            dispatcher.connect(self.thread_finished, signal=Thread_señal, sender=Thread_sender)
            for event in pygame.event.get():    # Catch all the pygame events.
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:  # If a key is pressed:
                    if event.key == pygame.K_SPACE:
                        print("Bombo Combo")
                        put = self.map.deploy_bomb(event.key)
                        if put == True:
                            time_explotion = self.map.Bomb.get_time()
                            self.thread = Thread(time_explotion)
                            self.thread.start()
                            print('entro')
                        self.view.load_sprite_bomb(event.key)
                    elif event.key == pygame.K_UP:  # If that key is 'up'
                        print("up")
                        self.view.change_tntman_sprite(str(event.key))
                        if self.map.is_position_valid(CONTROLS
                                                      [str(event.key)]):
                            self.map.move_tm(CONTROLS[str(event.key)])
                    elif event.key == pygame.K_DOWN:  # If that key is 'down'
                        print("down")
                        self.view.change_tntman_sprite(str(event.key))
                        if self.map.is_position_valid(CONTROLS
                                                      [str(event.key)]):
                            self.map.move_tm(CONTROLS[str(event.key)])
                    elif event.key == pygame.K_RIGHT:  # If that key is 'right'
                        print("right")
                        self.view.change_tntman_sprite(str(event.key))
                        if self.map.is_position_valid(CONTROLS
                                                      [str(event.key)]):
                            self.map.move_tm(CONTROLS[str(event.key)])
                    elif event.key == pygame.K_LEFT:  # If that key is 'left'
                        print("left")
                        self.view.change_tntman_sprite(str(event.key))
                        if self.map.is_position_valid(CONTROLS
                                                      [str(event.key)]):
                            self.map.move_tm(CONTROLS[str(event.key)])
                    elif event.key == pygame.K_t:
                        self.map.easter_egg()
                    self.view.reload_background()
                    self.view.reload_tntman()
                    self.view.load_blocks()
            
                if self.map.is_there_any_bomb() is True:
                    """ In case there is a bomb, the main loop will"""
                    self.view.reload_bomb()

                    # self.clock.tick()
                    # self.bombtime = self.bombtime + self.clock.get_time()
                    # if self.bombtime > 3000:
                    # self.map.destroy_bomb()

                pygame.display.flip()  # Updates screen.


if __name__ == "__main__":  # This function runs first.
    driver = Driver()  # Creates the Driver.
