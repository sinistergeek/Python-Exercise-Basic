import tkinter as tk
mw = tk.Tk()
mc = tk.Canvas(mw, width = 200,height = 200)
line = mc.create_line(200,0,0,200,200,200,200,0,fill="orange")
mc.pack()
mw.mainloop()
