import sqlite3

# create the database
connection = sqlite3.connect("coffee_data.db")

# establish a table within the database we just created
with connection:
    connection.execute("CREATE TABLE beans (id INTEGER PRIMARY KEY, "
                       "                    name TEXT,"
                       "                    method TEXT,"
                       "                    rating INTEGER")
