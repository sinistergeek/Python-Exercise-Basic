import mysql.connector as msql

dbConfig={'user':'root','password':'root','host':'localhost','database':'pymysql'}
pycon = msql.connect(**dbConfig)
print(pycon)
pycon.close()
