def addNumber(number):
    if number==5:
        return
    print(number +1)
    number+=1
    addNumber(number)
    
def summation(number):
    if number==1:
        return number
    else :
        return number+summation(number-1)
    
x=summation(5)
print(x)