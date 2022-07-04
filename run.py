from sys import argv

from functions import db_functions as my_db
from functions import json_functions as js_func


# books = js_func.open_json("./jsons/books.json")

books = my_db.open_books() or {}
print(books)
new_books = {}

for item in range(0, int(argv[1])):
	new_books[item + len(books)] = {
		"ID": item + len(books),
		"Title": input("Title: "),
		"Author": input("Author: "),
		"Translator": input("Translator: "),
		"Year": int(input("Year: ")),
		"Pages": int(input("Pages: ")),
		"Owned": int(input("Owned (1 for true 0 for false): ")) > 0,
		"Origin": input("Country of Origin: "),
		"Price": int(input("Price: "))
	}

print(new_books)

for book in new_books:
	my_db.save_book(new_books[book])