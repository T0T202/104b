#Assignment 3 Problem 3

import numpy as np
import math
#Define dimension of a vector
d = int(input("Please enter the dimensions of the vector: "))
#Define the 2 vector array
v1 = []
v2 = []

#First vector
print("Please enter the components for the first vector: ")
for i in range(0 ,d):
    v1i = int(input())
    v1.append(v1i)

#Second vector
print("Please enter the components for the second vector: ")
for i in range (0, d):
    v2i = int(input())
    v2.append(v2i)

#Cross Product
cross = []
cross.append(v1[1]*v2[2] - v1[2]*v2[1])
cross.append(v1[2]*v2[0] - v1[0]*v2[2])
cross.append(v1[0]*v2[1] - v1[1]*v2[0])

print("The cross product of the 2 vector is: ", cross[0],"i + ", cross[1], "j + ",cross[2],"k")


sum = 0 #The sum of all the elements squared in an array for cross product vector
sum1 = 0 #vector 1
sum2 = 0 #vector 2
for i in range (0, d):
    sum = sum + cross[i] ** 2
    sum1 = sum1 + v1[i] ** 2
    sum2 = sum2 + v2[i] ** 2
cross_length = np.sqrt(sum)
v1_length = np.sqrt(sum1)
v2_length = np.sqrt(sum2)

print("Sine of the angle between two vectors is: ", cross_length/(v1_length*v2_length))
print("The value of the angle is: ", math.asin(cross_length/(v1_length*v2_length)), " radians")