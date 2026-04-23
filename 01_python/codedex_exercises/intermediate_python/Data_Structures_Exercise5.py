## Aufgabe: 
""" 
Imagine you have a dataset with information about your favorite sports team. 🏀🎾⚽ The goal is to use Python's data structures to organize and analyze this data.

If you can't think of any, feel free to use the Super Bowl 2024 champions, the Kansas City Chiefs. 🏈

As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

Let's start analyzing!

    Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
    Print out a list of all player positions in the dataset.
    Choose a player and update their game statistics in the dataset.
    Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.

"""
# Ursprüngliche Version
tyreek = {'name': 'Tyreek Hill', 'position': 'Wide Receiver', 'jersey_number': 10, 'yards_gained': 150, 'touchdowns': 2}
jefferson = {'name': 'Justin Jefferson', 'position': 'Wide Receiver', 'jersey_number': 18, 'yards_gained': 137, 'touchdowns': 1}
mahomes = {'name': 'Patrick Mahomes', 'position': 'Quarterback', 'jersey_number': 15, 'yards_gained': 312, 'touchdowns': 3}
henry = {'name': 'Derrick Henry', 'position': 'Running Back', 'jersey_number': 22, 'yards_gained': 189, 'touchdowns': 2}

print(tyreek["name"],tyreek["position"])
print(jefferson["name"],jefferson["position"])
print(mahomes["name"],mahomes["position"])
print(henry["name"],henry["position"])


mahomes["touchdowns"] += 2
print(mahomes["touchdowns"])

avg_touchdowns = (tyreek["touchdowns"] + jefferson["touchdowns"] + mahomes["touchdowns"] + henry["touchdowns"])/4
print(avg_touchdowns)

# Version 2
players = [
    {'name': 'Tyreek Hill', 'position': 'Wide Receiver', 'jersey_number': 10, 'yards_gained': 150, 'touchdowns': 2},
    {'name': 'Justin Jefferson', 'position': 'Wide Receiver', 'jersey_number': 18, 'yards_gained': 137, 'touchdowns': 1},
    {'name': 'Patrick Mahomes', 'position': 'Quarterback', 'jersey_number': 15, 'yards_gained': 312, 'touchdowns': 3},
    {'name': 'Derrick Henry', 'position': 'Running Back', 'jersey_number': 22, 'yards_gained': 189, 'touchdowns': 2}
]

"""
Leitfrage List Comprehension: 
„Kann man den Code noch in einem Satz auf Deutsch beschreiben?"
Wenn ja → List Comprehension. Wenn nein → normale Schleife.
"""

names = [player["name"] for player in players] # für jeden Spieler in der Spielerliste trage bitte den Namen in eine neue Liste ein
print("Alle registrierten Spieler: ",names)

positions = [player["position"] for player in players]
print("Die jeweiligen Positionen: ",positions)

players[1]["touchdowns"] += 3
players[1]["yards_gained"] += 50
print("Angepasste Touchdowns und Yards bei: ", players[1]["name"], players[1]["touchdowns"], players[1]["yards_gained"]) 

all_yards = sum(player["yards_gained"] for player in players)
avg_yard = all_yards / len(players)
print("Durchschnittliche Yards", avg_yard)

all_touchdowns = sum(player["touchdowns"] for player in players)
avg_td = all_touchdowns / len(players)
print("Durchschnittliche Touchdowns: ", avg_td)

