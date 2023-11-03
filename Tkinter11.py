import tkinter as tk
mw = tk.Tk()
mc = tk.Canvas(mw, width = 200,height = 200)
rect = mc.create_rectangle(5,10,100,50,fill = "Purple", width=5,outline="Red",activefill ="yellow")
mc.pack()
mw.mainloop()
