#Assignment 2 - Problem 2

import numpy as np
import matplotlib.pyplot as plt

#Enter the number of points
number = int(input('Enter the number of points: '))

#Define array of x and y
x = []
y = []

#Enter the coordinates of x and y 
for i in range(0, number):
    xi = float(input('Enter x: '))
    x.append(xi)
    yi = float(input('Enter y: '))
    y.append(yi)
    #Define all parameters - A, B, C, D - coefficients of 2 linear equations and N - number of points define in line 6
    # m*A + b*B = C
    # m*B + b*N = D
    a = b = c = d = 0
    a = a + x[i]**2
    b = b + x[i]
    c = c + x[i]*y[i]
    d = d + y[i]

#Print out the list of coordinates
list_coordi = ''
for i in range (0, number):
    list_coordi = list_coordi + '(' + str(x[i]) + ',' + str(y[i]) + ')\n'
print('\nList of coordinates: ',list_coordi)

#Print out the value for all coefficients
print('A: ', a, 'B: ', b, 'C: ', c, 'D: ', d)

#Finding the value of m (the slope) and b0 (y-intercept) based on the value of A, B, C, D
m = (number*c - b*d)/((number)*a-b**2)
print('The slope is: ',m)

b0 = (c - m*a)/b
print('The y-intercept is: ', b)

#Maximum value of x = end point
max_x = np.max(x)

#Define an array of x-value from 0 to end point
x_vals = np.arange(0, max_x+1, 1)

#Define an array of y-value by computing y = mx + b
y_vals = m*x_vals + b0

#Plot the line based on the value of m and b0
plt.plot(x, y, 'bo', label = 'Coordinates')
plt.plot(x_vals, y_vals, '--', label = 'Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()