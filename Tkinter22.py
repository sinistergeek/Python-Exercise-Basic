import tkinter as tk
mw = tk.Tk()
mc = tk.Canvas(mw,bg="pink",width=400,height=400)
fnt = ('Times',15,"bold")
txt = mc.create_text(150,50, text = "Black and White", font = fnt,fill="black",activefill="white")
mc.pack()
mw.mainloop()
