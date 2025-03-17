import pygame
from components import *

def team_selection_screen(screen, font, game_state):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (0, 255, 0)
    GRAY = (128, 128, 128)
    screen.fill(WHITE)

   
    drawText(screen, font, "Select Your Team", 600, 100, BLUE, center=True)
    font = pygame.font.Font(None, 24)  

    
    teams = [
        "Spokane Snowmen", "Boise Potatoes", "Bismarck Lightning", "Cheyenne Vikings", "Salt Lake City Saints",
        "Portland Hornets", "Columbus Clouds", "Albany Rats", "Madison Polar Bears", "Richmond Spiders",
        "Tuscon Stars", "Monterey Demons", "Odessa Gamblers", "Tulsa Toucans", "Carlsbad Bats",
        "Jackson Scouts", "Greenville Blitzers", "Macon Waffles", "Daytona Racers", "Memphis Smashers"
    ]
    
    teams_per_row = 5  
    team_width = 200   
    team_height = 60   
    team_spacing = 20  
    start_x = 50       
    start_y = 250      

    def select_team(team):
        print(f"Team selected: {team}")
        game_state["selected_team"] = team  
        game_state["current_screen"] = "calendar"  

    
    for i, team in enumerate(teams):
        row = i // teams_per_row
        col = i % teams_per_row

        x = start_x + col * (team_width + team_spacing)
        y = start_y + row * (team_height + team_spacing)

        button(screen, font, x, y, team_width, team_height, team, lambda t=team: select_team(t))
