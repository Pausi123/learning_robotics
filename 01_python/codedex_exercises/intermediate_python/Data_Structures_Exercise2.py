## Aufgabe: 
""" 
Thanks to the internet, we can connect with friends across the world. 🧑‍🤝‍🧑

When you and your friends are scattered across different cities, sharing locations is something that can help you feel closer. 🌐

Let's use latitude and longitude to create tuples of our friends locations!

    Create a tuple for the city you are in.
    Create 3 tuples for your friends, each with the latitude and longitude of their cities.
    Print the locations of all your friends.

Which of your friends is the furthest away?

Bonus: See if you can combine all the tuples into one tuple.
"""

dennis_loc = (52.0, 8.5)
flo_loc = (50.8, 7.5)
svenja_loc = (51.6, 7.6)
jupp_loc = (51.8, 6.6) 

print("Alle Locations als einzelne Tuple: ",dennis_loc, flo_loc, svenja_loc, jupp_loc)

comb_loc = dennis_loc + flo_loc + svenja_loc + jupp_loc

print("Alle Locations als kompiniertes Tuple: ", comb_loc)