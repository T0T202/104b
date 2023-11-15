#Assignment 2 - Problem 3
import numpy as np
from numpy import linalg as la
from scipy.sparse import diags
import matplotlib.pyplot as plt

#Create the matrix with [-J, E, -J] along the main diagonal, to achieve the same format for the first line and the last line, set the offset of -J to -1 and 1 so -J will be adjusted by 1 unit along the diagonal
a = diags([-0.9, 2.4, -0.9], [-1,0,1], shape=(33,33)).toarray()
print(a)

#Use numpy to calculate the eigenvalues and eigenvectors of the matrix
# w - eigenvalues matrix
# v - eigenvectors matrix
w, v = la.eig(a)

print("The eigenvalues are: \n",w)
plt.hist(w, bins='auto')
plt.show()