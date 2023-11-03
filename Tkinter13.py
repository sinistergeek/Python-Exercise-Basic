import tkinter as tk
mw=tk.Tk()
mc=tk.Canvas(mw,width=200,height=200)
rect=mc.create_rectangle(50,25,150,100,outline="Red")
arc=mc.create_arc(50,25,150,100)
mc.pack()
mw.mainloop()
