import sqlite3

def save_book(book_data={}, filename="books.db", directory="./database/books/", table_name="books"):
	con = sqlite3.connect(directory + filename)
	cur = con.cursor()
	
	try:
		cur.execute("""CREATE TABLE {f} (id, title, author, translator, year, pages, owned, origin, price)""".format(f=table_name))
	except Exception as e:
		print(e)

	cur.execute("INSERT INTO {f} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)".format(f=table_name), (book_data["ID"], book_data["Title"], book_data["Author"], book_data["Translator"], book_data["Year"], book_data["Pages"], book_data["Owned"], book_data["Origin"], book_data["Price"]))

	con.commit()
	con.close()


def open_books(filename="books.db", directory="./database/books/", table_name="books"):
	con = sqlite3.connect(directory + filename)
	cur = con.cursor()

	books = {}
	try:
		for row in cur.execute("SELECT * FROM {f} ORDER BY id".format(f=table_name)):
			print(row[1])
			books[row[0]] = {
				"ID": row[0],
				"Title": row[1],
				"Author": row[2],
				"Translator": row[3],
				"Year": row[4],
				"Pages": row[5],
				"Owned": row[6] == 1,
				"Origin": row[7],
				"Price": row[8]
			}
	except Exception as e:
		print(e)
	return books
