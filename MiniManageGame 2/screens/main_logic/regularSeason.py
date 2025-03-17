import random

conferences = {
    "Northern": {
        "West": ["Spokane Snowmen", "Boise Potatoes", "Bismarck Lightning", "Cheyenne Vikings", "Salt Lake City Saints"],
        "East": ["Columbus Clouds", "Albany Rats", "Madison Polar Bears", "Richmond Spiders", "Portland Hornets"]
    },
    "Southern": {
        "West": ["Tucson Stars", "Monterey Demons", "Odessa Gamblers", "Tulsa Toucans", "Carlsbad Bats"],
        "East": ["Jackson Scouts", "Greenville Blitzers", "Macon Waffles", "Daytona Racers", "Memphis Smashers"]
    }
}

def generate_schedule_for_team(selected_team, conferences):
    schedule = []
    day = 1 
    
    for conference, divisions in conferences.items():
        for division, teams in divisions.items():
            if selected_team in teams:
                opponents = [t for t in teams if t != selected_team]
                for opponent in opponents:
                    for _ in range(6):  
                        schedule.append({"day": day, "team": selected_team, "opponent": opponent})
                        day += 1
                break  

    for conference, divisions in conferences.items():
        division_1, division_2 = divisions.values()
        if selected_team in division_1:
            for team in division_2:
                for _ in range(3):
                    schedule.append({"day": day, "team": selected_team, "opponent": team})
                    day += 1
        elif selected_team in division_2:
            for team in division_1:
                for _ in range(3):
                    schedule.append({"day": day, "team": selected_team, "opponent": team})
                    day += 1

    if selected_team in conferences["Northern"]["West"] + conferences["Northern"]["East"]:
        other_conference_teams = conferences["Southern"]["West"] + conferences["Southern"]["East"]
    else:
        other_conference_teams = conferences["Northern"]["West"] + conferences["Northern"]["East"]

    for opponent in other_conference_teams:
        for _ in range(3):
            schedule.append({"day": day, "team": selected_team, "opponent": opponent})
            day += 1

    return schedule

'''
schedule = generate_schedule(conferences)
for game in schedule[:20]:  # Print first 20 games as a sample
    print(game)
'''
