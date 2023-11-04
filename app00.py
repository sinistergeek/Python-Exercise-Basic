import tkinter as tk
import mysql.connector as msql
import credential as c

def create_tab():
    pycon = msql.connect(**c.dbConfig)
    mycursor = pycon.cursor()
    statement = "CREATE TABLE "+str(table_name_E.get())+"("+str (column1_E.get())+", "+str(column2_E.get())+", "+str(column3_E.get())+", "+str(column4_E.get())+""+str(column5_E.get())+", "+" PRIMARY KEY("+str(columnpk_E.get())+"));"
    print("Passing following information to MySQL textile database:"+statement)
    mycursor.execute(statement)
    pycon.close()

mw=tk.Tk()
mw.geometry('500x500')
table_name = tk.Label(mw, text='TABLE NAME')
table_name.place(x=10,y=10)

table_name_E = tk.Entry(mw,bd=2)
table_name_E.place(x=100,y=10)

column1 = tk.Label(mw,text='Column1')
column1.place(x=10,y=60)

column1_E = tk.Entry(mw,bd=2)
column1_E.place(x=100,y=60)

column2 =tk.Label(mw,text='Column2')
column2.place(x=10,y=110)

column2_E = tk.Entry(mw,bd=2)
column2_E.place(x=100,y=110)

column3 = tk.Label(mw,text='Column3')
column3.place(x=10,y=160)

column3_E = tk.Entry(mw,bd=2)
column3_E.place(x=100,y=160)

column4=tk.Label(mw, text='Column4')
column4.place(x=10,y=210)

column4_E=tk.Entry(mw,bd=2)
column4_E.place(x=100,y=210)

column5=tk.Label(mw,text='Column5')
column5.place(x=10,y=260)

column5_E=tk.Entry(mw,bd=2)
column5_E.place(x=100,y=260)

columnpk=tk.Label(mw,text='PKEY')
columnpk.place(x=10,y=310)

columnpk_E =tk.Entry(mw,bd=2)
columnpk_E.place(x=100,y=310)

create_button = tk.Button(mw,text='CREATE TABLE',command=create_tab)
create_button.place(x=40,y=360)
mw.mainloop()
