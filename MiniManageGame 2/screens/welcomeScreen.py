import pygame
import sys
import os
from components import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main_logic')))  #from google, use for other functions, ended up putting mani logic inside screens
from main_logic import games
from main_logic.players import *


wins = 0
losses = 0

def welcome_screen(screen, font, screen_state):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255,0,0)
    screen.fill(WHITE)
    screen_state["current_screen"] = "welcome"
    drawText(screen, font, "Welcome to the Baseball Management Game!", 600, 100, BLUE, center=True)
    drawText(screen, font, "Pick a team and Manage them to the world series.", 600, 200, RED, center=True)

    def start_game():
        screen_state["current_screen"] = "team_selection"
        pygame.display.flip()
        print("Switching to team selection screen...")  
        
        all_players = generate_all()
        free_agents = generate_free_agents()
        all_players.extend(free_agents)
        

    def quit_game():
        pygame.quit()
        sys.exit()

    button(screen, font, 450, 300, 300, 50, "Start Game", start_game)
    button(screen, font, 450, 400, 300, 50, "Quit", quit_game)
