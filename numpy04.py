import matplotlib.pyplot as plt
import numpy as np
start = int(input("Enter the starting point of the range : "))
end = int(input("Enter the end point of the range : "))
step = int(input("Enter the interval between two consecutive values : "))
x = np.arange(start,end,step)
y = (x**2) + (3*x)
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("plotting of function")
plt.show()
