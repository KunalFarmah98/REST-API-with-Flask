import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# INTEGER is used to create auto incrementing id on new entry addition
create_table = "CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS Items(name text, price real)"
cursor.execute(create_table)