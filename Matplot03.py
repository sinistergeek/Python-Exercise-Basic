#import the pyplot module from matplotlib libarary
import matplotlib.pyplot as plt

#define two lists for the values of x and y
x = [10,20,30,40,50,60,70,80,90]
y = [7,14,21,28,35,42,49,56,63]

#Call the plot(x,y) function. Also provide the color and style for the #point. Here we are going for green square point.
plt.plot(x,y, 'gs')
#Display the plot
plt.show()

