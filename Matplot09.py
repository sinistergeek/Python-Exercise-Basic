#import the pyplot module from matplolib library
import matplotlib.pyplot as plt

#define two lists for the values of x1 and y1
x1 = [10,20,30,40,50,60,70,80,90]
y1 = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function for values of x1 and y1
plt.plot(x1,y1)

#define two lists for the values of x2 and y2

x2 = [7,14,21,28,35,42,49,56,63]
y2 = [10,20,30,40,50,60,70,80,90]

#Call the plot(x,y) function for values of x2 and y2
plt.plot(x2,y2)

#label the x-axis
plt.xlabel('X-axis')
#label the y-axis
plt.ylabel('Y-axis')

#Give a title to the graph
plt.title('Plotting two lines on the same graph using Pyplot')
#Display the plot
plt.show()
