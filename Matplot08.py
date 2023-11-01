#import the pyplot module from matplotlib library
import matplotlib.pyplot as plt

#define two lists for the values of x and y
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function
plt.plot(x,y)

#Label the x-axis
plt.xlabel('X-axis')

#Label the y-axis
plt.ylabel('Y-axis')

#Give a title to the graph
plt.title('Simple Line Plot using pyplot')

#Display the plot
plt.show()
