#Assignment 3 Problem 2

import numpy as np

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
sum = 0
#Calculate the dot product between 2 vector
for i in range(0, d):
    sum = sum + v1[i] * v2[i]

print("The dot product of the 2 vectors is: ", sum)