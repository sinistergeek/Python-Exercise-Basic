import sqlite3

conn = sqlite3.connect("sample.db")
c = conn.cursor()

my_company = 'Acme'

try:
    c.execute('''INSERT INTO companies (name) VALUES (?)''',(my_company,))
except sqlite3.IntegrityError as e:
    print('sqlite error: ', e.args[0])
conn.commit()

companies = [('foo',12),('Bar',7),('Moo',99)]

try:
    sql = '''INSERT INTO companies (name, employees) VALUES (?, ?)'''
    c.executemany(sql,companies)
except sqlite3.IntegrityError as e:
    print('sqlite error:', e.args[0])
conn.commit()
conn.close()
print('done')
