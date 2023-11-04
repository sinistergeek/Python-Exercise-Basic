import mysql.connector as msql
import credential as c
pycon=msql.connect(**c.dbConfig)
print(pycon)
pycon.close()
