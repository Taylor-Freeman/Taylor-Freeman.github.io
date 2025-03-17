import random
import numpy as np
import os


TEAM_PITCHERS = 280  # 14 pitchers per team × 20 teams
TEAM_POSITION_PLAYERS = 240  # 12 position players per team × 20 teams
FREE_AGENTS = 130  # Mix of pitchers and position players

POSITION_QUOTAS = {
    "C": 20,   # 1 catcher per team
    "1B": 20,  # 1 first baseman per team
    "2B": 20,  # 1 second baseman per team
    "3B": 20,  # 1 third baseman per team
    "SS": 20,  # 1 shortstop per team
    "LF": 20,  # 1 left fielder per team
    "CF": 20,  # 1 center fielder per team
    "RF": 20,  # 1 right fielder per team
    "DH": 20,   # 1 designated hitter per team
    "Extra": 60 # 3 extra bench players per team (I think the players should be randomly assigned not in same order, not sure if matters anyway)
}

position_counts = {position: 0 for position in POSITION_QUOTAS}
pitcher_count = 0
free_agent_count = 0

TEAMS = ["Spokane Snowmen", "Boise Potatoes", "Bismarck Lightning", "Cheyenne Vikings", "Salt Lake City Saints",
"Portland Hornets", "Columbus Clouds", "Albany Rats", "Madison Polar Bears", "Richmond Spiders",
"Tuscon Stars", "Monterey Demons", "Odessa Gamblers", "Tulsa Toucans", "Carlsbad Bats",
"Jackson Scouts", "Greenville Blitzers", "Macon Waffles", "Daytona Racers", "Memphis Smashers"] 
FREE_AGENT_TEAM = "Free Agent"

class Player:
    def __init__(self, Name, Age, Country, Position, Hitting_Stat=None, Fielding_Stat=None, Speed=None, 
    Pitching_Stat=None, Contract_Salary=0, Contract_Year=0, Is_Pitcher=False,Team=None):
        self.name = Name
        self.age = Age
        self.country = Country
        self.position = Position
        self.hitting_stat = Hitting_Stat
        self.fielding_stat = Fielding_Stat
        self.speed = Speed
        self.pitching_stat = Pitching_Stat
        self.contract_salary = Contract_Salary
        self.contract_year = Contract_Year
        self.is_pitcher = Is_Pitcher
        self.team = Team


def load_names(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

FIRST_NAMES = load_names('FirstName.txt')
LAST_NAMES = load_names('LastName.txt')


def assign_team(player_index):
    if player_index < TEAM_PITCHERS:  
        team_index = player_index // 14
        return TEAMS[team_index]
    elif player_index < TEAM_PITCHERS + TEAM_POSITION_PLAYERS:  
        team_index = (player_index - TEAM_PITCHERS) // 12
        return TEAMS[team_index]
    else:                                                  
        return FREE_AGENT_TEAM


def assign_position(is_pitcher=False, is_free_agent=False):
    global pitcher_count
    if is_pitcher:
        if pitcher_count < TEAM_PITCHERS + FREE_AGENTS:
            pitcher_count += 1
            return "P"
    else:
        if is_free_agent:
            return random.choice(list(POSITION_QUOTAS.keys()))
        else:
            available_positions = [pos for pos, count in position_counts.items() if count < POSITION_QUOTAS[pos]]
            if not available_positions:
                raise ValueError("No positions left for team players!")
            position = random.choice(available_positions)
            position_counts[position] += 1
            return position




def generate_player(player_index, is_free_agent=False):
    name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    age = random.randint(18, 40)
    country = random.choice(["USA", "Canada", "Japan", "Dominican Republic", "Cuba", "Venezuela", "China", "Puerto Rico", "Mexico", "United Kingdom"])
    is_pitcher = player_index < TEAM_PITCHERS or (player_index >= TEAM_PITCHERS + TEAM_POSITION_PLAYERS and random.choice([True, False]))
    position = assign_position(is_pitcher, is_free_agent)
    team = assign_team(player_index)

    if is_pitcher:
        return Player(
            Name=name, Age=age, Country=country, Position=position, Team=team,
            Fielding_Stat=randomStat(),
            Pitching_Stat=randomStat(),
            Contract_Salary=random.uniform(0.5, 20),
            Contract_Year=random.randint(1, 5),
            Is_Pitcher=True
        )
    else:
        return Player(
            Name=name, Age=age, Country=country, Position=position, Team=team,
            Hitting_Stat=randomStat(),
            Fielding_Stat=randomStat(),
            Speed=randomStat(),
            Contract_Salary=random.uniform(0.5, 20),
            Contract_Year=random.randint(1, 5),
            Is_Pitcher=False
        )



def randomStat():
    return random.randint(50,99)

def generate_all():
    players = []
    global pitcher_count
    total_position_players = TEAM_POSITION_PLAYERS  
    total_pitchers = TEAM_PITCHERS  

    for i in range(650):
        print(f"Generated Players: {len(players)}, Pitchers: {pitcher_count}, Position Players: {sum(position_counts.values())}")

        if pitcher_count >= total_pitchers and sum(position_counts.values()) >= total_position_players:
            print(f"All quotas met. Total players generated: {len(players)}")
            break

        if pitcher_count < total_pitchers:
            players.append(generate_player(i))  
        elif sum(position_counts.values()) < total_position_players:
            players.append(generate_player(i))  

    return players

def generate_free_agents():
    players = []
    for i in range(FREE_AGENTS):
        player = generate_player(player_index=TEAM_PITCHERS + TEAM_POSITION_PLAYERS + i, is_free_agent=True)
        players.append(player)
    return players


def count_players_by_team(players):
    team_counts = {}
    for player in players:
        if player.team in team_counts:
            team_counts[player.team] += 1
        else:
            team_counts[player.team] = 1
    return team_counts
'''
all_players = generate_all()
free_agents = generate_free_agents()
all_players.extend(free_agents)

team_counts = count_players_by_team(all_players)

# Print the results
for team, count in team_counts.items():
    print(f"{team}: {count} players")


all_players = generate_all()

players = [player for player in all_players if player.team == "Spokane Snowmen"]

for player in players:
    print(f"Name: {player.name}, Position: {player.position}, Team: {player.team}")
'''