def collatz(n):
    #Check if n > 1
    while (n>1):
        print(n)
        #Check if n is odd
        if ((n % 2) != 0):
            n = 3*n + 1
        #If n is even
        else:
            n = n // 2
    print(1)

n = int(input('Enter n: '))
print('Sequence: ')
collatz(n)