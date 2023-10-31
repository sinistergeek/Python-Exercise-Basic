import mysql.connector as msql
pycon = msql.connect(host='localhost',user='root',passwd='root',charset='utf8',database='pymysql')
mycursor = pycon.cursor()
statement = 'select * from pymysql.book;'
mycursor.execute(statement)
mycursor.fetchall()
mycursor.execute("""INSERT INTO book(chapter,pages) VALUES("Basics","15");""")
pycon.commit()
statement = 'select * from book;'
mycursor.execute(statement)
mycursor.fetchall()
