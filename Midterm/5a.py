a = int(input("Please enter the quadratic formula: "))
b = int(input("Please enter the quadratic formula: "))
c = int(input("Please enter the quadratic formula: "))

r1 = (-b-((b**2 - 4*a*c)**(0.5)))/2*a

r2 = (-b+((b**2 - 4*a*c)**(0.5)))/2*a
print(r1, "\t", r2)