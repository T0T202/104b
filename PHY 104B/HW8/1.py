import numpy as np

#Create initial cell with random distribution of 1 and 0
cell = np.random.randint(2, size=13)
#Create an empty array to store updated cell
newcell = np.empty(13, dtype=int)
print('t = 0 :\t',cell)
# print(newcell)

for i in range(0, 20):
    for j in range(0, 13):
            if(j == 0):
                if((cell[12] == 0 & cell[j] == 0 & cell[j+1] == 0)):
                    newcell[j] = 0
                if((cell[12] == 0 & cell[j] == 0 & cell[j+1] == 1)):
                    newcell[j] = 1
                if((cell[12] == 0 & cell[j] == 1 & cell[j+1] == 0)):
                    newcell[j] = 1
                if((cell[12] == 0 & cell[j] == 1 & cell[j+1] == 1)):
                    newcell[j] = 1
                if((cell[12] == 1 & cell[j] == 0 & cell[j+1] == 0)):
                    newcell[j] = 1
                if((cell[12] == 1 & cell[j] == 0 & cell[j+1] == 1)):
                    newcell[j] = 0
                if((cell[12] == 1 & cell[j] == 1 & cell[j+1] == 0)):
                    newcell[j] = 1
                if((cell[12] == 1 & cell[j] == 1 & cell[j+1] == 1)):
                    newcell[j] = 0
            elif(j == 12):
                if((cell[j-1] == 0 & cell[j] == 0 & cell[0] == 0)):
                    newcell[j] = 0
                if((cell[j-1] == 0 & cell[j] == 0 & cell[0] == 1)):
                    newcell[j] = 1
                if((cell[j-1] == 0 & cell[j] == 1 & cell[0] == 0)):
                    newcell[j] = 1
                if((cell[j-1] == 0 & cell[j] == 1 & cell[0] == 1)):
                    newcell[j] = 1
                if((cell[j-1] == 1 & cell[j] == 0 & cell[0] == 0)):
                    newcell[j] = 1
                if((cell[j-1] == 1 & cell[j] == 0 & cell[0] == 1)):
                    newcell[j] = 0
                if((cell[j-1] == 1 & cell[j] == 1 & cell[0] == 0)):
                    newcell[j] = 1
                if((cell[j-1] == 1 & cell[j] == 1 & cell[0] == 1)):
                    newcell[j] = 0
            else:
                if((cell[j-1] == 0 & cell[j] == 0 & cell[j+1] == 0)):
                    newcell[j] = 0
                if((cell[j-1] == 0 & cell[j] == 0 & cell[j+1] == 1)):
                    newcell[j] = 1
                if((cell[j-1] == 0 & cell[j] == 1 & cell[j+1] == 0)):
                    newcell[j] = 1
                if((cell[j-1] == 0 & cell[j] == 1 & cell[j+1] == 1)):
                    newcell[j] = 1
                if((cell[j-1] == 1 & cell[j] == 0 & cell[j+1] == 0)):
                    newcell[j] = 1
                if((cell[j-1] == 1 & cell[j] == 0 & cell[j+1] == 1)):
                    newcell[j] = 0
                if((cell[j-1] == 1 & cell[j] == 1 & cell[j+1] == 0)):
                    newcell[j] = 1
                if((cell[j-1] == 1 & cell[j] == 1 & cell[j+1] == 1)):
                    newcell[j] = 0
    print('t = ', i+1, ':\t', newcell)
    for k in range(0, 13):
        cell[k] = newcell[k]
        