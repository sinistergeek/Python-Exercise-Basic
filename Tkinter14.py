import tkinter as tk
mw=tk.Tk()
mc=tk.Canvas(mw,width=200,height=200)
arc=mc.create_arc(50,25,150,100,start=120,extent=90)
mc.pack()
mw.mainloop()
