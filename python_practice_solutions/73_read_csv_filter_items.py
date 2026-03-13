
import csv

with open("books.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["price"]) > 50:
            print(row)
