#Assignment 6 - Problem 1
import numpy as np
from numpy import linalg as la
from scipy.sparse import diags

#Create the matrix with [-J, E, -J] along the main diagonal, to achieve the same format for the first line and the last line, set the offset of -J to -1 and 1 so -J will be adjusted by 1 unit along the diagonal
# J = 1 and E = 0
a = diags([-1, 0, -1], [-1,0,1], shape=(7,7)).toarray()
print(a)

#Use numpy to calculate the eigenvalues and eigenvectors of the matrix
# w - eigenvalues matrix
# v - eigenvectors matrix
w, v = la.eig(a)

#Create another matrix - which is the transpose of the eigenvectors matrix
v_T = v.T

print("The eigenvalues are: \n",w)

#The real and imaginary matrices  - obtained by multiply eigenvalues with its corresponding eigenvectors and its transpose
t = 0.1
# Real matrix - with t from 0 to 4
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix - with t from 0 to 4
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(t*w[n]))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues) for the real matrix

            e_i[i][j] = e_i[i][j] + ((np.sin(t*w[n]))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues) for the imaginary matrix

print("The real matrix: \n", e_real)
print("The imaginary matrix: \n",e_i)
