import tkinter as tk
import tkinter.messagebox



def message_display():
    tk.messagebox.showinfo("Wellcome Note","Hello world!")
mw = tk.Tk()

mw.geometry("150x150")
my_first_button = tk.Button(mw, text="Click Here", command = message_display)
my_first_button.pack()
mw.mainloop()
