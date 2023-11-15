answer = 42000
count = 0

while count <6:
    guess = int(input("Guess:"))
    if(count<5):
        if(guess < answer):
            print("Too low")
            count = count +1
        elif(guess > answer):
            print("Too high")
            count = count + 1
        else:
            print("You won the car")
            break
    else:
        print("Too many guess")
        break