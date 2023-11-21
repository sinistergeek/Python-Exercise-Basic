import sys
import os
import sqlite3

database_file = "counter.db"

def usage():
    print('TODO print doc')
    conn.close()
    exit()

def main():
    global conn
    conn = sqlite3.connect(database_file)
    c=conn.cursor()
    try:
        c.execute('''CREATE TABLE counters(id PRIMARY KEY,name VARCRCHAR(100),UNIQUE NOT NULL,count INTEGER NOT NULL)''')
    except sqlite3.OperationalError as e:
        pass


    if len(sys.argv) == 1:
        usage()

    if len(sys.argv) ==2:
        if sys.argv[1] == '--list':
            print('List counters')
            for r in c.execute("SELECT name FROM counters"):
                print(r[0])
            exit()
        name = sys.argv[1]
        c.execute("SELECT count FROM counters WHERE name = ?",(name,))
        line = c.fetchone()
        if line == None:
            print("Invalid counter name '{}'".format(name))
            exit()
        value = line[0]
        value  =  value + 1
        c.execute("UPDATE counters SET count=? WHERE name = ?",(value,name))
        conn.commit()
        print("{} {}".format(name,value))
        exit()

    if len(sys.argv) == 3 and sys.argv[1] == '--start':
        name = sys.argv[2]
        print("Start counter",name)
        try:
            c.execute("INSERT INTO counters(name,count) VALUES(?,?)",(name,0))
            conn.commit()
        except sqlite3.IntegrityError:
            print("Name '{}' already exists".format(name))
            exit()
        exit()
    print('none')
    usage()
main()
