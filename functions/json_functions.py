import json
import sqlite3 as sql3

def open_json(filename):
	# print(filename)
	with open(filename) as json_file:
		return json.load(json_file)

def save_json(filename="", json_data={}):
	with open(filename, "w") as json_file:
		json.dump(json_data, json_file, indent=4)

def sort_by_shelf(json_data={}, shelf="Psychology", category="-bs"):
	sort_category = {
		"-bs": "Shelves",
		"-bo": "Origin"
	}
	b = {}
	for book in json_data:
		if shelf.title() in json_data[book][sort_category[category]]:
			b[book] = json_data[book]
	return b

def get_prices(json_data={}, category=""):
	price = 0
	for book in json_data:
		if not json_data[book]["Owned"] and category == "Price":
			price += json_data[book][category]
		elif category == "Pages":
			price += json_data[book][category]
	return price

def json_to_sqlite(json_data={}, directory="./database/", filename="books", new=True):
	connect_main = sql3.connect(directory + filename + ".db")
	cursor_main = connect_main.cursor()
	
	try:
		cursor_main.execute('''CREATE TABLE books (id, title, author, year, pages, owned, origin, price, amazon)''')
	except Exception as e:
		print(e)

	for book in json_data:
		cursor_main.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (book, json_data[book]["Title"], json_data[book]["Author"][0], json_data[book]["Year"], json_data[book]["Pages"], json_data[book]["Owned"], json_data[book]["Origin"], json_data[book]["Price"], json_data[book]["Amazon"]))
		
	connect_main.commit()

	connect_main.close()
