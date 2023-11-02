import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,4,7,9,10,14])
y = 4*x+6
plt.plot(x,y,"rs--",markersize=6,linewidth =3)
plt.xlabel("x")
plt.ylabel("y=4x+6")
plt.show()
