import random

def calculate_hit_probability(hitter_stat, pitcher_stat):
    """Calculate the probability of a hit based on hitter and pitcher stats."""
    base_chance = hitter_stat - pitcher_stat + 50
    return max(0, min(base_chance, 100))  

def determine_hit_type():
    """Determine the type of hit based on weighted probabilities."""
    hit_type = random.choices(
        ["Single", "Double", "Triple", "Home Run"],
        weights=[60, 25, 10, 5]  
    )[0]
    return hit_type

def simulate_at_bat(hitter_stat, pitcher_stat):
    """Simulate a single at-bat based on hitter and pitcher stats."""
    hit_chance = calculate_hit_probability(hitter_stat, pitcher_stat)
    walk_chance = 10  
    strikeout_chance = 100 - hit_chance - walk_chance  
    
    
    outcome = random.uniform(0, 100)
    if outcome < hit_chance:
        return determine_hit_type()  
    elif outcome < hit_chance + walk_chance:
        return "Walk"
    else:
        return "Out"

def advance_runners(bases, hit_type):
    runs = 0
    
    if hit_type == "Single":
        runs += sum(1 for base in bases if base)  
        bases = [True] + bases[:-1]  
    elif hit_type == "Double":
        runs += sum(1 for base in bases if base)  
        bases = [None, True] + bases[:-2]  
    elif hit_type == "Triple":
        runs += sum(1 for base in bases if base)  
        bases = [None, None, True]  
    elif hit_type == "Home Run":
        runs += sum(1 for base in bases if base) + 1  
        bases = [None, None, None]  
    
    return bases, runs

def simulate_inning(lineup, pitcher_stat):
    outs = 0
    runs = 0
    bases = [None, None, None]  
    
    while outs < 3:
        hitter_stat = lineup.pop(0)  
        lineup.append(hitter_stat)  
        result = simulate_at_bat(hitter_stat, pitcher_stat)
        
        if result == "Out":
            outs += 1
        elif result == "Walk":
            
            if bases[0] and bases[1] and bases[2]:  
                runs += 1  
            bases = [True if i == 0 else bases[i-1] for i in range(3)]
        elif result in ["Single", "Double", "Triple", "Home Run"]:
            bases, scored = advance_runners(bases, result)
            runs += scored
            print(f"{result}! Runs scored: {scored}")
            
    return runs

import random

def simulate_game(home_lineup, away_lineup, home_pitcher_stat, away_pitcher_stat):
    home_score = 0
    away_score = 0
    
    for inning in range(1, 10):
        print(f"Inning {inning}:")
        
        away_runs = simulate_inning(away_lineup, home_pitcher_stat)
        away_score += away_runs
        print(f"Away team scored {away_runs} runs. Total: {away_score}")
        
        home_runs = simulate_inning(home_lineup, away_pitcher_stat)
        home_score += home_runs
        print(f"Home team scored {home_runs} runs. Total: {home_score}")
    
    if home_score == away_score:
        print("Game is tied! Deciding winner by coin flip...")
        winner = random.choice(["Home", "Away"])
        print(f"The winner is decided by coin flip: {winner} team wins!")
    else:
        winner = "Home" if home_score > away_score else "Away"
        print(f"The winner is the {winner} team!")
    
    return {
        "home_score": home_score,
        "away_score": away_score,
        "winner": winner
    }

