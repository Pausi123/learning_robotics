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