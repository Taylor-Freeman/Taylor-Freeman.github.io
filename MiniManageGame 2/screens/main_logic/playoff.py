import random

standings = {
    "Spokane Snowmen": {"wins": 0, "losses": 0},
    "Boise Potatoes": {"wins": 0, "losses": 0},
    "Bismarck Lightning": {"wins": 0, "losses": 0},
    "Cheyenne Vikings" : {"wins": 0, "losses": 0},
    "Salt Lake City Saints" : {"wins": 0, "losses": 0},
    "Columbus Clouds" : {"wins": 0, "losses": 0},
    "Albany Rats" : {"wins": 0, "losses": 0},
    "Madison Polar Bears": {"wins": 0, "losses": 0},
    "Richmond Spiders" : {"wins": 0, "losses": 0},
    "Portland Hornets" : {"wins": 0, "losses": 0},
    "Tucson Stars" : {"wins": 0, "losses": 0},
    "Monterey Demons" : {"wins": 0, "losses": 0}, 
    "Odessa Gamblers" : {"wins": 0, "losses": 0},
    "Tulsa Toucans" : {"wins": 0, "losses": 0},
    "Carlsbad Bats" : {"wins": 0, "losses": 0},
    "Jackson Scouts" : {"wins": 0, "losses": 0},
    "Greenville Blitzers" : {"wins": 0, "losses": 0},
    "Macon Waffles" : {"wins": 0, "losses": 0}, 
    "Daytona Racers" : {"wins": 0, "losses": 0},
    "Memphis Smashers" : {"wins": 0, "losses": 0}
}

def simulate_playoff_round(teams, series_length):
    winners = []
    for i in range(0, len(teams), 2):
        team1, team2 = teams[i], teams[i+1]
        wins1, wins2 = 0, 0
        while wins1 < series_length // 2 + 1 and wins2 < series_length // 2 + 1:
            winner = random.choice([team1, team2])
            if winner == team1:
                wins1 += 1
            else:
                wins2 += 1
        winners.append(team1 if wins1 > wins2 else team2)
    return winners

def playoffs():
    #Wildcard Round
    wildcard_teams = ["2nd_seed", "3rd_seed"]  
    wildcard_winners = simulate_playoff_round(wildcard_teams, 3)
    
    #Division Series
    division_teams = ["1st_seed"] + wildcard_winners
    division_winners = simulate_playoff_round(division_teams, 5)

    #Conference Series
    conference_winners = simulate_playoff_round(division_winners, 7)

    #World Series
    world_series_winner = simulate_playoff_round(conference_winners, 7)
    print(f"The World Series champion is {world_series_winner[0]}!")

playoffs()
