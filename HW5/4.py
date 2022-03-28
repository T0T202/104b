#Assignment 5 - Problem 4
import numpy as np
from numpy import linalg as la
from scipy.sparse import diags

#Create the matrix with [-J, E, -J] along the main diagonal, to achieve the same format for the first line and the last line, set the offset of -J to -1 and 1 so -J will be adjusted by 1 unit along the diagonal
a = diags([-0.9, 2.4, -0.9], [-1,0,1], shape=(33,33)).toarray()
print(a)

#Use numpy to calculate the eigenvalues and eigenvectors of the matrix
# w - eigenvalues matrix
# v - eigenvectors matrix
w, v = la.eig(a)

#Create another matrix - which is the transpose of the eigenvectors matrix
v_T = v.T

print("The eigenvalues are: \n",w)

#The result matrix (exponential) - obtained by multiply eigenvalues (exponential) with its corresponding eigenvectors and its transpose
# e = e^(-0.3 a)
e = np.zeros(shape=(33,33)) #create a 33x33 matrix
for n in range(0, 33): #loop n times with different eigenvalues
    for i in range(0, 33): #loop i times to get complete rows
        for j in range(0, 33): #loop j times to get complete columns
            e[i][j] = e[i][j] + ((np.exp(-0.3*w[n]))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
np.set_printoptions(threshold=np.inf)
print("The exponential matrix: \n",e)