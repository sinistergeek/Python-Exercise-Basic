import sqlite3

conn = sqlite3.connect("sample.db")
c = conn.cursor()
try:
    c.execute('''CREATE TABLE companies(id PRIMARY KEY,name VARCHAR(100) UNIQUE NOT NULL,employees INTEGER DEfAULT 0)
              ''')
except sqlite3.OperationalError as e:
    print('sqlite error',e.args[0])
conn.commit()
conn.close()
print('done')
