import tkinter as tk
mw = tk.Tk()
mc = tk.Canvas(mw, width=200,height=200)
line = mc.create_line(0,0,200,200,fill = "Blue")
mc.pack()
mw.mainloop()
