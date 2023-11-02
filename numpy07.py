import matplotlib.pyplot as plt
import numpy as np
x = ['John','Ted','Lizy','Elena','Alex','Albert','Meg']
arr = np.array([367,455,478,300,260,345,400])
y = arr*100/500
plt.bar(x,y)
plt.xlabel("Student name")
plt.ylabel("%score")
plt.title("Score")
plt.show()
