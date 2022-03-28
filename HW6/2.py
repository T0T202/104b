#Assignment 6 - Problem 2
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
psi_r = np.zeros #real part of psi
psi_i = np.zeros #imaginary part of psi

fig, axs = plt.subplots(9, sharey = True) #Creating 9 subplots with the same y - axis
fig.suptitle('Probability at different time')
#The real and imaginary matrices  - obtained by multiply eigenvalues with its corresponding eigenvectors and its transpose

# At t = 0
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix 
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*0))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n]*0))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)


psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[0].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 0.5
# Real matrix
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*0.5))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n]*0.5))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[1].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 1
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n]))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[2].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 1.5
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*1.5))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n])*1.5)*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[3].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 2
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*2))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n])*2)*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[4].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 2.5
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*2.5))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n])*2.5)*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[5].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 3
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*3))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n])*3)*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[6].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 3.5
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*3.5))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n])*3.5)*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[7].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')

#At t = 4
# Real matrix 
e_real = np.zeros(shape=(7,7)) #create a 7x7 matrix

# Imaginary matrix
e_i = np.zeros(shape=(7,7)) #create a 7x7 matrix

for n in range(0, 7): #loop n times with different eigenvalues
    for i in range(0, 7): #loop i times to get complete rows
        for j in range(0, 7): #loop j times to get complete columns
            e_real[i][j] = e_real[i][j] + ((np.cos(w[n]*4))*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)
            e_i[i][j] = e_i[i][j] + ((np.sin(w[n])*4)*v[i][n] * v_T[n][j]) #adding the previous saved elements of the matrix with the next elements(different eigenvalues)

psi_r = np.matmul(e_real, psi_0)
psi_i = np.matmul(e_i, psi_0)

for i in range(0, 7):
    axs[8].plot(i, psi_r[i] ** 2 + psi_i[i] ** 2, 'ko')
np.set_printoptions(threshold=np.inf)

print("The real matrix: \n",e_real)
print("The imaginary matrix: \n",e_i)
print("The real psi: \n", psi_r)
print("The imaginary psi: \n", psi_i)


plt.legend()
plt.show()