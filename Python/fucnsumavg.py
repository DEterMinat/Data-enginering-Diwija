def summation(number):
    total,avg=0,0
    for i in number:
        total+=i
    avg=total/len(number)
    return total,avg

x=[1,2,3]
y=summation(x)
print(y)
