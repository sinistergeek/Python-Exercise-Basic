import tkinter as tk

mw = tk.Tk()

labelusern=tk.Label(mw, text = "User Name")
labelpwd = tk.Label(mw,text = "Password")
entryusern = tk.Entry(mw, width=20)
entrypwd = tk.Entry(mw, width=20)
loginButton = tk.Button(mw, text = 'Login')

labelusern.place(x =10,y=5)
labelpwd.place(x=10,y=40)
entryusern.place(x=75,y=5)
entrypwd.place(x =75,y=40)
loginButton.place(x=10,y=80)
mw.mainloop()
