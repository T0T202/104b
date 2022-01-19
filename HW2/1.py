import numpy as np
import matplotlib.pyplot as plt

#Define parameters
#ODE
f = lambda x, y: -x*y
#Step size
h = 0.10
#Numerical grid
x = np.arange(0, 1+h, h)
#Initial condition
y0 = 7

#Assignment 1 Euler Method
y = np.zeros(len(x))
y[0] = y0 #assigned initial condition to the array
for i in range(0, len(x) - 1):
    y[i+1] = y[i] + h*f(x[i], y[i])
print('For first method, at x = 1, the value of y is: ', y[len(x)-1])

#Assignment 2, second method
y1 = np.zeros(len(x))
y1[0] = y0 #assigned the initial condition to the array
for i in range(0, len(x)-1):
    y1[i+1] = y1[i] + h*((3*f(x[i], y1[i])/2) -(f(x[i-1],y1[i-1])/2))
print('For first method, at x = 1, the value of y is: ', y1[len(x)-1])

#Assignment 2, third method
y2 = np.zeros(len(x))
y2[0] = y0 #assigned the initial condition to the array
for i in range (0, len(x)-1):
    y2[i+1] = ((1-h*x[i]/2)/(1+h*x[i+1]/2))*y2[i]
print('For first method, at x = 1, the value of y is: ', y2[len(x)-1])

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo--', label = 'First method')
plt.plot(x, y1, 'ro--', label = 'Second method')
plt.plot(x, y2, 'ko--', label = 'Third method')
plt.plot(x, (7 * np.exp(-((x**2)/2))), 'g', label = 'Exact solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#Discuss
#Based on what we get from the graph, both new methods have better accuracy than the one we did in assignment 1, the third method gives the best approximation compared to the others. But when x is about 0.8, the solutions for the second method and the third method seems to overlap each other