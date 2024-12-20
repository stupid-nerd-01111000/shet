from sqlite3 import connect


with connect('conn.db') as a:
    cursor = a.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS goodby (id INTEGER)')
