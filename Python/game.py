number=int(input("number :"))
for row in range(number):
    for column in range(number):
        if row ==0 or row == number-1 or column == 0 or column == number-1:
            print("X",end='')
        else:
            print(" ",end='')
    print(" ")