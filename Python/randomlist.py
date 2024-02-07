number = []
while True:
    x=int(input("input your num: "))
    if x<0:
        break
    number.append(x)
    
number.sort()
print(number)
print("End")
    