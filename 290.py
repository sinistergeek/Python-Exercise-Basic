import sqlite3

conn = sqlite3.connect("sample.d")
c = conn.cursor()

minimum = 0

sql = '''SELECT * FROM companies WHERE employees >= ?'''
for company in c.execute(sql,(minimum,)):
    print(company)

sql = '''SELECT COUNT(*) FROM companies WHERE employees >= ?'''
print(c.fetchone()[0])

conn.close()
