#Assignment 3 Problem 1

import numpy as np

#Define dimension of a vector
d = int(input("Please enter the dimensions of the vector: "))
#Define the vector array
v = []
#Initial sum of all the elements in the array (to the power of 2)
sum = 0
#Run loops according to the dimension of the vector
for i in range(0, d):
    vi = int(input())
    v.append(vi)
    #Calculate the total sum of all the elements squared
    sum = sum + vi ** 2

#Normalize the vector by taking the square-root of the sum
norm = np.sqrt(sum)
#Run loops to calculate its unit length
for i in range(0, d):
    v[i] = v[i] / norm

#Print out the final result
print("After normalizing: ", v)