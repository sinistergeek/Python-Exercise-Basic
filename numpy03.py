#import numpy
import numpy as np

#import PyPlot
import matplotlib.pyplot as plt

#define array have values from 20 to 40, 5 values apart
x = np.arange(20,40,5)

#define f(x) = log(x)
y = np.log(x)

#Call the plot() function
plt.plot(x,y)

#Label the X-axis
plt.xlabel("x values from 20-40, 5 steps apart")

#Label the Y-axis
plt.ylabel("f(x) vs. x")

#Give a title to the plot
plt.title("f(x) vs. x")

#Display the plot
plt.show()
