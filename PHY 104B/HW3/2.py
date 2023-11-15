#Assignment 3 Problem 2

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

#initial sum 
dot = 0 #use to calculate the dot product
sum1 = 0 #use to calculate the length of vector 1
sum2 = 0 #use to calculate the length of vector 2
#Calculate the dot product between 2 vector
for i in range(0, d):
    dot = dot + v1[i] * v2[i]
    #The length of each vector
    sum1 = sum1 + v1[i] ** 2
    sum2 =  sum2 + v2[i] ** 2
v1_length = np.sqrt(sum1)
v2_length = np.sqrt(sum2)

print("The dot product of the 2 vectors is: ", dot)
print("The cosine value of the angle between 2 vectors is: ", dot/(v1_length * v2_length))
print("The angle between the 2 vectors is: ", math.acos(dot/(v1_length * v2_length)))