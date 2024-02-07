max,min =0,0

while True:
    number = int(input("Number :"))
    if number < 0:
        break
    if number>max:
        max = number
    if number<min:
        min = number
print("Max :",max)
print("Min :",min)

