import pygame
import random
from components import *
from welcomeScreen import wins, losses

# Global variables
your_outs = 0
opp_outs = 0
your_score = 0
opp_score = 0
running = True

def simulation_screen(screen, font, game_state):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)

    global your_outs
    global opp_outs
    global your_score
    global opp_score
    global running
    global wins
    global losses

    smallerfont = pygame.font.Font(None, 24)
    smallfont = pygame.font.Font(None, 30)

    selected_team_name = game_state["selected_team"]

    drawText(screen, font, "Matchup", 600 , 100, BLUE, center=True)
    drawText(screen, smallfont, "vs.", 600 , 400, BLUE, center=True)
    drawText(screen, font, selected_team_name, 250, 400, RED, center=True)
    drawText(screen, font, "Opponent", 900, 400, RED, center=True)

    def game_play():
        global your_outs
        global opp_outs
        global your_score
        global opp_score
        global running
        global wins
        global losses

        '''
        result = ['out', 'single', 'double', 'triple', 'HR']
        weights = [40, 30, 15, 10, 5]
        '''
        

        while your_outs < 3:
            result = ['out', 'single', 'double', 'triple', 'HR']
            weights = [40, 30, 15, 10, 5]
            type = random.choices(result, weights)[0]
            print(type)
            if type == 'single':
                your_score += 1
            elif type == 'double':
                your_score += 2
            elif type == 'triple':
                your_score += 3
            elif type == 'HR':
                your_score += 4
            elif type == 'out':
                your_outs += 1
            print(your_score)

        while opp_outs < 3:
            result = ['out', 'single', 'double', 'triple', 'HR']
            weights = [40, 30, 15, 10, 5]
            opp_type = random.choices(result, weights)[0]
            print(opp_type)
            if opp_type == 'single':
                opp_score += 1
            elif opp_type == 'double':
                opp_score += 2
            elif opp_type == 'triple':
                opp_score += 3
            elif opp_type == 'HR':
                opp_score += 4
            elif opp_type == 'out':
                opp_outs += 1

        if opp_outs == 3 and your_outs == 3:
            print("a =" + str(your_score))
            print("b =" + str(opp_score))
            game_state["current_screen"] = "event"
            pygame.display.flip()    

    button(screen, font, 450, 600, 300, 50, "Hit", game_play)

    #pygame.display.flip() 

