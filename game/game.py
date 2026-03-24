

import pygame
import sys
import config as con
from game.player import Player
from game.utils import clamp_position

# Hazards
from game.hazard_manager import HazardManager
import game.hazards as hz


class Game:
    def __init__(self):
        pygame.init()

        # display setup
        self.screen = pygame.display.set_mode((con.WINDOW_SIZE_X, con.WINDOW_SIZE_Y))
        pygame.display.set_caption("BHTG")

        # clock
        self.clock = pygame.time.Clock()

        # tp indicator
        self.tp_indicator = pygame.Surface((con.PLAYER_SIZE * 2, con.PLAYER_SIZE * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.tp_indicator, (0, 0, 0, 50), (con.PLAYER_SIZE, con.PLAYER_SIZE), con.PLAYER_SIZE)

        self.running = True
        self.player = Player([con.WINDOW_SIZE_X / 2, con.WINDOW_SIZE_Y / 2])

        self.hazard_manager = HazardManager()
        self.hazard_manager.add_hazard(hz.CircleZone([60, 100], 50, 5, 200, 200))
        self.hazard_manager.add_hazard(hz.CircleZone([700, 600], 50, 10, 800, 100))
        self.hazard_manager.add_hazard(hz.CircleZone([60, 600], 50, 15, 500, 50))
        for i in range(100):
            self.hazard_manager.add_hazard(hz.StraightBullet([i*10, 0], i+1, [0, 1], i*4, 10))




    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0

            self.handle_events()
            self.update(dt)
            self.draw()

        self.cleanup()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.player.teleport(mouse_x, mouse_y)

    def update(self, dt):
        self.player.update(dt)
        
        state = self.hazard_manager.collision(self.player.pos)

        if state:
            print("You lost")
            self.cleanup()

        self.hazard_manager.update_hazards(dt)


    def draw(self): 
        # clear screen
        self.screen.fill((100, 100, 100))

        # get mouse pos
        mouse_x, mouse_y = pygame.mouse.get_pos()
        indicator_x, indicator_y = clamp_position(mouse_x, mouse_y)

        # draw indication circle
        current_color = (0, 255, 0, 50) if self.player.cooldown <= 0 else (255, 0, 0, 50) # choose color
        surface = pygame.Surface((con.PLAYER_SIZE*2, con.PLAYER_SIZE*2), pygame.SRCALPHA)  # creates new Surface 
        pygame.draw.circle(surface, current_color, (con.PLAYER_SIZE, con.PLAYER_SIZE), con.PLAYER_SIZE) # draws a circle on the surface
        self.screen.blit(surface, (indicator_x - con.PLAYER_SIZE, indicator_y - con.PLAYER_SIZE)) # draws the entire surface with the circle

        # draw line for help 
        pygame.draw.line(self.screen, current_color, self.player.pos, (indicator_x, indicator_y), 1)

        # Draw player
        pygame.draw.circle(self.screen, (0, 0, 0), self.player.pos, con.PLAYER_SIZE)


        # Draw hazards
        self.hazard_manager.draw_hazards(self.screen)

        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
        sys.exit()



