import tkinter as tk
mw = tk.Tk()
mc = tk.Canvas(mw, width=350,height=350)
mc.create_oval(20,20,200,200,fill="yellow")
mc.pack()
mw.mainloop()
