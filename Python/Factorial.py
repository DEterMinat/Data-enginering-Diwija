def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)
    
x=factorial(5)
print(x)