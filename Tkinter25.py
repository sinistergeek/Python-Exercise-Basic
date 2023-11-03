import tkinter as tk
import time

start_time = 0
end_time = 0
total_time = 0
def time_display(seconds):
    minutes = seconds//60
    hours = minutes//60
    minutes = minutes%60
    seconds = seconds%60
    msg = "Time Lapsed = {0}:{1}:{2}".format(int(hours),int(minutes),int(seconds))
    lbl = tk.Label(mw,text = msg,fg="blue",bg="white",font=("Monospace",14,"bold italic"),width=100,height=100)
    lbl.pack(side = "top")

def timer_start():
    global start_time
    print("in start time")
    start_time = time.time()
    print(start_time)

def timer_end():
    end_time = time.time()
    total_time = end_time = start_time
    time_display(int(total_time))

mw = tk.Tk()
mw.geometry('300x300')
mf = tk.Frame(mw)

mf.pack(side = "bottom")
button1 = tk.Button(mf, text = "Start",bg="green",bd=10,command=timer_start)
button1.pack(side="left")
button2 = tk.Button(mf,text="Stop",bg="red",bd=10,command=timer_end)
button2.pack(side = "right")
mw.mainloop()

