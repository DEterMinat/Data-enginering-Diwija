import random 

myRandom = random.randrange(1,7)

while True:
    number = int(input("Enter a number between 1 and 6 : "))
    if number == myRandom:
        print("You Win")
        break
    elif number < myRandom:
        print("Your number is too low")
    elif number > myRandom:
        print("Your number is too high")
    