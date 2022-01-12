# import numpy as np
# import matplotlib.pyplot as plt

#Differential Equation dy/dx = -xy
def DiffEq(x, y):
    return(-x*y)

#Euler method, x0 = initial x, h = step size
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

#declare an array of y values 
y_app = []

#iterating the euler method with different values of h
for i in range(0,6):
    Euler(x0, y0, h[i],x)
    y_app.append(y0)
    i = i+1
#The analytical solution for this differential equation at x = 1.2 is y = 3.40727
print (y_app)


