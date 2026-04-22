## Aufgabe: 
""" 
As one of the cultural capitals of the world, NYC is the home of the Met Museum. 🏛️

It has one of the biggest art collections in the world!

Let’s catalog an artifact from the museum! 🖼️ 👩‍🎨

First, search the Met Museum site for your favorite artifact. Scroll to "Artwork Details" and let's start cataloging.

On the Python editor, create a dictionary with the information of your artifact, including:

    artist
    period
    date

Lastly, print the dictionary. What do you see? What if we just want to print the keys, or the values?
"""

artifact = {
  'name' : "Bronze statuette of a young woman",
  'artist' : "Not known", 
  'date' : "late 6th century BCE",
  'period' : "Archaic",
}

print(artifact)
print(artifact.keys())
print(artifact.values())