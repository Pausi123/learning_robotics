## Aufgabe: 
""" 
Moving day is almost here! As you gather your belongings, the thought of packing everything can feel overwhelming. 😥

Using what we learned about files in Python, let’s make a program to help manage your packing list.

First, in a .py file, import the csv module. Then, paste the following:

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

We're gonna use this data to make a CSV file!

Next, create a try-except statement. For the try block:

    Try opening a packing_list.csv file in 'r' "read" mode.
    Create a reader object for the CSV file.
    Loop through and print() each row in the object .

For the except block:

    Specify the FileNotFoundError.
    Print "Packing list file not found. Creating a new one."
    Open a new packing_list.csv file in 'w' "write" mode.
    Create a writer object of the CSV file.
    Use the object's .writerows() method to process the data variable.

At this point, go ahead and save your .py file and run your program once.

Look in your file system and you should see a new CSV file in the same folder as this file.

Nice, you did it! Go ahead and add more things to your packing list and share with your friends to have them double check!

Happy packing! 📦
"""

import csv

csv_path = '/home/denpau/Nitro5_Ubuntu_sync/Biomechatronik/Learning_Robotik/01_python/codedex_exercises/intermediate_python/packing_list.csv'

# Each inner list = one CSV row; first row is the header
data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

# Try to read first — only create the file if it doesn't exist yet
try :
    with open(csv_path, 'r', encoding='utf-8') as file:  # 'with' closes the file automatically, even on error
        csv_reader = csv.reader(file)  # wraps the file so it understands CSV formatting (commas, quotes, etc.)
        for row in csv_reader:
            print(row)  # each row is a plain Python list, e.g. ['Blender', '2']
except FileNotFoundError:  # only catches this specific error — other errors still crash the program
    print("Packing list file not found. Creating a new one.")
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:  # newline='' prevents double line breaks on Windows
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)  # writes all rows at once; use .writerow() (singular) for one row at a time