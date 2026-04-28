## Aufgabe: 
""" 
Diaries can contain anything and everything. Some have even won awards. 🤫 Regardless of what your writing aspirations may be, let’s make a diary. Your secret is safe with us (your local storage 🔐).

Let’s start writing!

    Use the open() method to create a new diaries.txt file.
    Fill your new diary with entries or secrets. 🤐
    Each entry should be separated by a new line.
"""
# File wird im Falschen Verzeichnis erstellt
#file = open('diaries.txt', 'w')
#file.write('Ich mag Züge !!!')

# Fix 1 Advanced:
#import os

# __file__ = Pfad dieser .py-Datei 
# → abspath macht ihn absolut → dirname schneidet Dateiname weg
#script_dir = os.path.dirname(os.path.abspath(__file__))
#filepath = os.path.join(script_dir, 'diaries.txt')

# Fix 2 Easy
file = open('/home/denpau/Nitro5_Ubuntu_sync/Biomechatronik/Learning_Robotik/01_python/codedex_exercises/intermediate_python/diaries.txt', 'w')
file.write("'Ich mag Züge !!!'")
file.close