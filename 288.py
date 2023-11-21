import sqlite3

conn = sqlite3.connect("sample.db")
c = conn.cursor()

conn.close()
