import numpy as np

#Define number of toss = n, number of heads = n_h, number of tails = n - n_h
n = 10
n_h = list(range(0,11))

#Calculate probability for number of heads by using for loop
for i in range(0, n):
    p = np.math.factorial(n)/((2**n)*(np.math.factorial(n_h[i]))*(np.math.factorial(10-n_h[i])))
    print('For NH = ', n_h[i], 'the probability is ' + '{:0.4f}'.format(round(p,4)), )

 