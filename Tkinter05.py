import tkinter as tk
import tkinter.messagebox as ag

def message_display_right():
    ag.showinfo("Next Topic", "Wellcome to Matrix")

def message_display_left():
    ag.showinfo("Previous Topic","Wellcome Neo")

mw = tk.Tk()
mw.title("Red or Blue pill")

my_first_button = tk.Button(mw,text="Blue Pill",fg="Blue",command = message_display_right)
my_second_button = tk.Button(mw,text="Red Pill",fg="Red",command = message_display_left)

my_first_button.pack(side = tk.RIGHT)
my_second_button.pack(side = tk.LEFT)
mw.mainloop()
