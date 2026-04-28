## Aufgabe: 
""" 
✨ Here at Codédex, we are 🤩 big fans of music 🎹. The only thing better than a perfect playlist is a playlist with all your favorite songs. Let's create a Python script that organizes the songs into a .txt file. Let's make a playlist!

First, let's define a dictionary to store liked songs:

liked_songs = {
  'title': 'artist'
}

Next, create a function to display and write liked songs to a file:

def write_liked_songs_to_file(liked_songs, file_name):

    Open the file in write mode.
    Write each song and artist by iterating through the liked_songs dictionary.

Your liked_songs.txt file should look something like this:

Liked Songs:
Bad Habits by Ed Sheeran
I'm Just Ken by Ryan Gosling
Mastermind by Taylor Swift
Uptown Funk by Mark Ronson ft. Bruno Mars
Ghost by Justin Bieber
"""

# Dictionary: Schlüssel = Songtitel, Wert = Künstler
# Global definiert, damit es unabhängig von der Funktion befüllt werden kann
liked_songs = {
    "Bad Habits" : "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber",
}

# Funktion nimmt Dictionary und Dateipfad als Parameter
# → wiederverwendbar für beliebige Dictionaries und Dateipfade
def write_liked_songs_to_file(songs, file_name):

    # 'w' = Write-Modus: Datei wird erstellt falls nicht vorhanden, sonst überschrieben
    # 'with' schließt die Datei automatisch nach dem Block
    with open(file_name, 'w') as file:
        # Überschrift schreiben, \n = Zeilenumbruch
        file.write("Liked Songs:\n")
        # .items() liefert alle Schlüssel-Wert-Paare
        # Unpacking direkt in title und artist — kein Index nötig
        for title, artist in songs.items():
            # f-String formatiert Titel und Künstler in eine lesbare Zeile
            file.write(f"{title} by {artist}\n")

# Funktionsaufruf mit Dictionary und absolutem Pfad zur Ausgabedatei
write_liked_songs_to_file(liked_songs, '/home/denpau/Nitro5_Ubuntu_sync/Biomechatronik/Learning_Robotik/01_python/codedex_exercises/intermediate_python/liked_songs.txt')
