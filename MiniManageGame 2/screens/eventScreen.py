import pygame
from gameSimulation import *
from components import *
from welcomeScreen import wins, losses
from gameSimulation import your_score, opp_score

def event_screen(screen, font, game_state):
    
    print(your_score)
    print(opp_score)

    global wins
    global losses
    
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    screen.fill(WHITE)
    
    smallerfont = pygame.font.Font(None, 24)
    smallfont = pygame.font.Font(None, 30)


    drawText(screen, font, "Your Score", 150, 350, GREEN, center=True)
    drawText(screen, font, "Opponent Score", 950, 350, GREEN, center=True)
    drawText(screen, font, str(your_score), 150, 450, BLUE, center=True)
    drawText(screen, font, str(opp_score), 950, 450, BLUE, center=True)

    drawText(screen, font, "Game Over", 600, 50, BLUE, center=True)
    if opp_outs < your_score:
        drawText(screen, font, "You Win!", 600, 700, GREEN, center=True)
        wins += 1
        print("a")
        pygame.display.flip()
    elif opp_outs > your_score:
        drawText(screen, font, "You Lose!", 600, 700, RED, center=True)
        losses += 1
        print("b")
        pygame.display.flip()
    elif opp_outs == your_score:
        bob = random.random()
        if bob < 0.5:
            drawText(screen, font, "You Win!", 600, 700, GREEN, center=True)
            wins += 1
            print("a")
            pygame.display.flip()
        else:
            drawText(screen, font, "You Lose!", 600, 700, RED, center=True)
            losses += 1
            print("b")
            pygame.display.flip()
        running = False 
    
    
    pygame.display.flip()

        

    def go_back():
        game_state["current_screen"] = "calendar"
        pygame.display.flip()

   
    button(screen, smallfont, 50, 50, 300, 50, "Go To Calendar", go_back)
