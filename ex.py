# dy / dx =(x + y + xy)
def func( x, y ):
    return (-x * y)
     
# Function for euler formula
def euler( x0, y, h, x ):
 
    # Iterating till the point at which we
    # need approximation
    while x0 < x:
        y = y + h * func(x0, y)
        x0 = x0 + h
 
    # Printing approximation
    print("Approximate solution at x = ", x, " is ", y)
     
# Driver Code
# Initial Values
x0 = 0
y0 = 7
h = 0.4
 
# Value of x at which we need approximation
x = 1.2
 
euler(x0, y0, h, x)