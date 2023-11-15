#Assignment 6 - Problem 1
import matplotlib.pyplot as plt
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


#psi at t = 0 has all components equal to zero except for the first component which is set to one
psi_0 = np.zeros(shape=(7,1)) 
psi_0[0][0] = 1
psi = np.zeros #psi after time t
prob = 0 #probability 
#The result matrix (exponential) - obtained by multiply eigenvalues (exponential) with its corresponding eigenvectors and its transpose
e = np.zeros(shape=(7,7)) #create a 7x7 matrix
# #For t = 0
# for n in range(0, 7): #loop n times with different eigenvalues
#         for i in range(0, 7): #loop i times to get complete rows
#             for j in range(0, 7): #loop j times to get complete columns
#                 e[i][j] = e[i][j] + (np.exp(0*w[n]*(-1 ** (1/2)))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
# psi = np.matmul(e, psi_0)
# for i in range(0,7):
#     plt.plot(i, psi[i]**2, 'o',label = 't=0')

#For t = 0.5
for n in range(0, 7): #loop n times with different eigenvalues
        for i in range(0, 7): #loop i times to get complete rows
            for j in range(0, 7): #loop j times to get complete columns
                e[i][j] = e[i][j] + (np.exp(0.5*w[n]*(-1 ** (1/2)))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
psi = np.matmul(e, psi_0)
for i in range(0,7):
    plt.plot(i, psi[i]**2, 'ko',label = 't=0.5')

np.set_printoptions(threshold=np.inf)
print("The exponential matrix: \n",e)
print("psi: \n", psi)
plt.legend()
plt.show()
