
import csv

books = [
    {"title": "Python Basics", "price": 50},
    {"title": "Java Guide", "price": 60}
]

with open("books.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(books)
