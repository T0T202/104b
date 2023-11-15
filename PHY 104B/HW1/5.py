#Number of integers
num = 1000
#Iteration length
iterationLength = 0
#Starting number 
startingNumber = 0
#Largest value
largestNumber = 0
#Largest value starting nummber
largestStartingNumber = 0
#Run loops of iteration from 0 to 1000
for i in range(0, 1001):
    length = 1
    n = i
#Check if n > 1
    while (n>1):
        #Check if n is odd
        if ((n % 2) != 0):
            n = 3*n + 1
        #If n is even
        else:
            n = n // 2
        length = length + 1
    if(n>largestNumber):
        largestNumber = n
        largestStartingNumber = i
    #Compare the current length of the loop with the previous longest iteration, if exceeds, assigned length to iterationLength and make starting number equal to i
    if (length > iterationLength):
        iterationLength = length
        startingNumber = i

print("The starting number is: ",startingNumber," and the number of iterations is: ", iterationLength)
print("The largest value is ", largestNumber, " and the starting number for that is ", largestStartingNumber)