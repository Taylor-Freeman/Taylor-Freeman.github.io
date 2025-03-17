import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main_logic')))
from components import *

from welcomeScreen import *
from teamSelect import *
from calendarScreen import *
#from roster import *
from gameSimulation import *
from main_logic.regularSeason import *
from eventScreen import *


pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Baseball Management Game")

WHITE = (255, 255, 255)
font = pygame.font.Font(None, 60)

game_state = {
    "current_screen": "welcome",
    "selected_team": None
}


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    if game_state["current_screen"] == "welcome":
        welcome_screen(screen, font, game_state)
    elif game_state["current_screen"] == "team_selection":
        team_selection_screen(screen, font, game_state)
    elif game_state["current_screen"] == "calendar":
        calendar_screen(screen, font, game_state)
    elif game_state["current_screen"] == "simulation":
        simulation_screen(screen, font, game_state)
    elif game_state["current_screen"] == "event":
        event_screen(screen, font, game_state)

    pygame.display.flip()

pygame.quit()
