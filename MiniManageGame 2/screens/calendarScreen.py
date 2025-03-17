import pygame
from components import *
from main_logic.regularSeason import *
from eventScreen import wins,losses

def calendar_screen(screen, font, game_state):
    selected_team = game_state["selected_team"]
    game_state["schedule"] = generate_schedule_for_team(selected_team, conferences)


    
    team_schedule = [game for game in game_state["schedule"] if game["team"] == selected_team]

    current_page = game_state.get("calendar_page", 0)  
    days_per_screen = 20
    start_index = current_page * days_per_screen
    end_index = start_index + days_per_screen
    days_to_display = team_schedule[start_index:end_index]

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    screen.fill(WHITE)
    smallerfont = pygame.font.Font(None, 24)
    smallfont = pygame.font.Font(None, 30)

    drawText(screen, font, "Upcoming Games", 600, 50, BLUE, center=True)
    drawText(screen, smallfont, selected_team, 600, 100, RED, center=True) 
    drawText(screen, font, "Record", 1075, 325, BLUE, center=True)
    drawText(screen, font, str(wins), 1025, 400, RED, center=True)
    drawText(screen, font, "-", 1075, 400, RED, center=True)
    drawText(screen, font, str(losses), 1125, 400, RED, center=True)
          
    
    for i, game in enumerate(days_to_display):
        row = i // 4  
        col = i % 4   
        x = 100 + col * 220  
        y = 150 + row * 120  

        day_text = f"Day {game['day']}"  
        opponent_text = f"vs {game['opponent']}"  
        drawText(screen, smallerfont, day_text, x, y, BLUE)
        drawText(screen, smallerfont, opponent_text, x, y + 40, RED)

    button_font = pygame.font.Font(None, 24)

    def prev_page():
        game_state["calendar_page"] = max(0, current_page - 1)  

    def next_page():
        max_pages = len(team_schedule) // days_per_screen
        game_state["calendar_page"] = min(max_pages, current_page + 1)  

    
    button(screen, button_font, 100, 700, 100, 50, "Previous", prev_page)

    
    button(screen, button_font, 1000, 700, 100, 50, "Next", next_page)

    def edit_roster():
        game_state["current_screen"] = "roster"
        pygame.display.flip()
    def play_next_game():
        game_state["current_screen"] = "simulation"  
        pygame.display.flip()  


    button(screen, smallerfont, 25, 25, 200, 40, "Play Next Game", play_next_game)
    button(screen, smallerfont, 975, 25, 200, 40, "Edit Roster", edit_roster) 

    pygame.display.flip()
