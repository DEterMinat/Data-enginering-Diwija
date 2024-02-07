number = []
while True:
    number.append(int(input("Number :")))
    if number[-1] == 0:
        break
    
number =[i*i for i in number]
print(number)