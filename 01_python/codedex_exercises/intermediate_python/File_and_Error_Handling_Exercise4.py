## Aufgabe: 
""" 
We've all seen, perhaps bought, one of our favorite products with a "Bestseller" sticker. 🏅

Let’s write a program to read a CSV file and find the best-selling book of all time. 🔍

    Download this CSV file of all-time bestselling books data!
    Open the Bestseller - Sheet1.csv file in "read" mode.
    Use the CSV reader to navigate through the data and find the book with the highest sales, via the sales in millions column.
    Create a new file called bestseller_info.csv with the CSV writer.
    In the new file, use .writerow() to add new CSV data.

Up next, let’s learn about what to do in the face of the unexpected, we'll be exploring error handling
"""

import csv

csv_file = "/home/denpau/Nitro5_Ubuntu_sync/Biomechatronik/Learning_Robotik/01_python/codedex_exercises/intermediate_python/Bestseller - Sheet1.csv"

csv_file_output = "/home/denpau/Nitro5_Ubuntu_sync/Biomechatronik/Learning_Robotik/01_python/codedex_exercises/intermediate_python/bestseller_info.csv"

max_sales = 0

with open(csv_file, "r", encoding='utf-8') as file:  # encoding='utf-8' required — CSV contains non-ASCII characters (e.g. Hindi)
    # Creates a reader object that wraps the file — no data is read yet.
    # The reader implements the iterator protocol: it only reads one line at a time
    # when explicitly asked (via for-loop or next()). This is memory-efficient
    # because it never loads the entire file at once.
    # When a line is read, the reader splits it at commas and returns it as a list:
    # "Book,Author,1939,100" → ["Book", "Author", "1939", "100"]
    csv_reader = csv.reader(file)

    #print(list(csv_reader))  # This will print the contents of the CSV file
    
    file.readline()  # Skip the header row; the Cursor knows automatically where the initial first line/row ends
    # alternatively, you can use next(csv_reader) to skip the header row

    for row in csv_reader:             # row is a list of strings — the reader parses one line and hands it over; each element is one column value
        current_sales = float(row[4])  # Assuming the sales in millions is in the fifth column (index 4)
        #print(current_sales)

        if current_sales > max_sales:
            max_sales = current_sales
            bestseller_book = row[0] 
            bestseller_author = row[1]


with open(csv_file_output, "w", newline='') as file:  # newline='' required — without it Python inserts blank lines between rows on Windows
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Book", "Author", "Sales"])
    csv_writer.writerow([bestseller_book, bestseller_author, max_sales])
