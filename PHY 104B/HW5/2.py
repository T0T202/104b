#Assignment 2 - Problem 2
import numpy as np
from numpy import linalg as la

#The original matrix from the problem
a = np.array([[4, 1, 0], [1, 4, 0], [0, 0, 2]])

#Use numpy to calculate the eigenvalues and eigenvectors of the matrix
# w - eigenvalues matrix
# v - eigenvectors matrix
w, v = la.eig(a)

print("The eigenvalues are: \n",w)
print("The eigenvectors corresponding to the eigenvalues are: \n", v)

#Create another matrix - which is the transpose of the eigenvectors matrix
v_T = v.T

#The result matrix (exponential) - obtained by multiply eigenvalues (exponential) with its corresponding eigenvectors and its transpose
# e = e^(-0.3 a)
e = np.zeros(shape=(3,3)) #create a 3x3 matrix
for n in range(0, 3): #loop n times with different eigenvalues
    for i in range(0, 3): #loop i times to get complete rows
        for j in range(0, 3): #loop j times to get complete columns
            e[i][j] = e[i][j] + ((np.exp(-0.3*w[n]))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
print("The exponential matrix: \n",e)
