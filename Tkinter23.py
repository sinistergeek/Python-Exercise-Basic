import tkinter as tk
mw = tk.Tk()
mf = tk.Frame(mw)
mf.pack()

button1 = tk.Button(mf,text="Red Pill",bg="red", bd=10)
button1.pack(side="left")

button2 = tk.Button(mf,text="Blue Pill",bg="Blue",bd=10)
button2.pack(side="right")

mw.mainloop()
