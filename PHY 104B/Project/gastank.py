from cProfile import run


running_sum1 = 0
running_sum2 = 0
print("Your Personal Fuel Economy")

while True:
    milestraveled = input("Number of miles traveled:")
    
    if milestraveled == "":
        if(running_sum2 == 0):
            print("Average: 0")
            break
        else:
            average = running_sum1/running_sum2
            average1d = float("{0:.1f}".format(average))
            print("Average:", average1d)
            break
    else:
        galneeded = input("Number of gallons: ")
        num1 = float(milestraveled)
        num2 = float(galneeded)
        tank = num1/num2
        tank1d = float("{0:.1f}".format(tank))
        print("Mileage this tank", tank1d)
        running_sum1 = running_sum1 + num1
        running_sum2 = running_sum2 + num2
    


