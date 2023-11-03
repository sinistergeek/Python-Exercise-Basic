import tkinter as tk

def arc_display():
    mc =tk.Canvas(mw,width=350,height=350)

    x0=int(input("Please enter the value of x0 : "))
    y0=int(input("Please enter the value of y0 : "))

    x1=int(input("Please enter the value of x1 : "))
    y1=int(input("Please enter the value of y1 : "))

    s_angle=int(input("Please enter the value for start angle : "))
    e_angle=int(input("Please enter the value for extent angel : "))
    
    mc.create_arc(x0,y0,x1,y1,start=s_angle,extent=e_angle)
    mc.pack()

mw=tk.Tk()
my_first_button=tk.Button(mw,text="Create Arc",command=arc_display)
my_first_button.pack()
mw.mainloop()
