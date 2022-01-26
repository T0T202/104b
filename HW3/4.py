#Assignment 3 Problem 4

import numpy as np

#Define N dimension 
print("Enter the dimension of the matrix: ")
n = int(input())
#Create matrix
matrix = np.zeros(shape=(n,n))
#Enter matrix
for j in range(0, n):
    for i in range(0, n):
        matrix[i][j] = float(input()) #Fill the matrix with each column (same j)
#Create vector with the same dimension
v = np.zeros(shape=(n,1))
#Enter elements of the vector
for i in range(0, n):
    v[i] = float(input())

#Result matrix of the application between the initial matrix and the vector
result = np.zeros(shape=(n,1))
#Initialize the sum of a row
sum_row = 0
#Number of times
m = int(input("Please enter M times: "))
#Normalize vector parameters
sum = 0 #The total sum of each elements in the result vector array squared
#Apply the matrix to the vector M times
for m in range(0, m):
    for i in range(0, n):
        for j in range(0, n):
            #Multiply rows of the matrix with column of the vector
            sum_row = sum_row + matrix[j][i] * v[j]
        result[i] = sum_row #Adding the result into the new matrix
        sum_row = 0 #Set the sum of a row back to 0, and begin the calculation again
        sum = sum + result[i]**2 #Get the sum of all the elements in the result array
    norm = np.sqrt(sum) #Calculate the normalization
    for i in range(0, n):
        result[i] = result[i]/norm #Divide the result vector by the square root of sum (which is the norm) to get its unit length
    sum = 0 #Set the sum of the elements back to 0, and begin the application again

print("The matrix is: \n", matrix)
print("The vector is: \n", v)
print("The result matrix is: \n", result)
