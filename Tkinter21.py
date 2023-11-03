import tkinter as tk
mw = tk.Tk()
mc = tk.Canvas(mw, width=150,height=350)
mc.create_polygon(250,30,200,50,230,90,60,300,100,20, fill="pink")
mc.pack()
mw.mainloop()
