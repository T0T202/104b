import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Differential Equation dy/dx = -xy
def DiffEq(x, y):
    return(-x*y)
#Euler method
def Euler(x0, y, h, x):
    while x0 < x:
        y = y + h * DiffEq(x0,y)
        x0 = x0 + h
    #Output approximation for x
    print("The approximation value at x = ",x," is ", y)
#Initial values
x0 = 0 
y0 = 7 
x = 1.2 

h = [0.40, 0.30, 0.20, 0.10, 0.05, 0.02] #different values of step size

#iterating the euler method with different values of h
for i in range(0,6):
    Euler(x0, y0, h[i],x)
    i = i+1

#compare value with different step size
    
# The analytical solution for this differential equation at x = 1.2 is y = 3.40727
# For h = 0.4, y = 3.9984
# For h = 0.02, y = 3.428852112667473

t = [1.2, 1.2, 1.2]
y = [3.40727, 3.9984, 3.428852112667473]
plt.plot(t,y, 'ko', label = 'compare')

#function that returns dy/dx
def model(y,x):
    dydx= -x*y
    return dydx

#initial condition 
y0 = 7

x = np.linspace(0, 2)

#solve differential equation
y = odeint(model, y0, x)

plt.plot(x,y, '-', label = 'analytical solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
#Based on the graph, we can see that, the approximation of y values are more accurate as the value of the step size 
#decreases