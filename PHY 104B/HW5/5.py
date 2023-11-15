#Assignment 5 - Problem 5
import numpy as np
from numpy import linalg as la
from scipy.sparse import diags
import matplotlib.pyplot as plt

#N = 129
#Create the matrix with [-J, E, -J] along the main diagonal, to achieve the same format for the first line and the last line, set the offset of -J to -1 and 1 so -J will be adjusted by 1 unit along the diagonal
a = diags([-0.9, 2.4, -0.9], [-1,0,1], shape=(129,129)).toarray()
print(a)

#Use numpy to calculate the eigenvalues and eigenvectors of the matrix
# w - eigenvalues matrix
# v - eigenvectors matrix
w1, v1 = la.eig(a)

print("The eigenvalues are: \n",w1)
plt.hist(w1, bins='auto')
plt.show()


#N = 513
#Create the matrix with [-J, E, -J] along the main diagonal, to achieve the same format for the first line and the last line, set the offset of -J to -1 and 1 so -J will be adjusted by 1 unit along the diagonal
b = diags([-0.9, 2.4, -0.9], [-1,0,1], shape=(129,129)).toarray()
print(b)

#Use numpy to calculate the eigenvalues and eigenvectors of the matrix
# w - eigenvalues matrix
# v - eigenvectors matrix
w2, v2 = la.eig(b)

print("The eigenvalues are: \n",w2)
plt.hist(w2, bins='auto')
plt.show()

