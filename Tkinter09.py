import tkinter as tk
mw=tk.Tk()
mc=tk.Canvas(mw,width=200,height=200)
#creater line
line = mc.create_line(200,0,0,200,fill="Purple",width=10)
line2 = mc.create_line(0,0,200,200,fill="Blue",width=10)
mc.pack()
mw.mainloop()
