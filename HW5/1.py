#Assignment 5 - Problem 1
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

#The result matrix (squared) - obtained by multiply eigenvalues (squared) with its corresponding eigenvectors and its transpose
f = np.zeros(shape=(3,3)) #create a 3x3 matrix
for n in range(0, 3): #loop n times with different eigenvalues
    for i in range(0, 3): #loop i times to get complete rows
        for j in range(0, 3): #loop j times to get complete columns
            f[i][j] = f[i][j] + ((w[n]**2)*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
print("The squared matrix: \n",f)

#The result matrix (inverse) - obtained by multiply eigenvalues (inverse) with its corresponding eigenvectors and its transpose
f_i = np.zeros(shape=(3,3)) #create a 3x3 matrix
for n in range(0, 3): #loop n times with different eigenvalues
    for i in range(0, 3): #loop i times to get complete rows
        for j in range(0, 3): #loop j times to get complete columns
            f_i[i][j] = f_i[i][j] + ((w[n]**(-1))*v[i][n] * v_T[n][j])#adding the previous saved elements of the matrix with the next elements(different eigenvalues)
print("The inverse matrix: \n",f_i)