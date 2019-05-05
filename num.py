import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1.0, 2.0, 3.0])
# y = np.array([1.0, 2.0, 3.0])
# print (x+y)
# print (x*y)

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label="sin")

plt.show()
