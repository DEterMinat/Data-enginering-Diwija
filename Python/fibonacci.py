def fibonacci(x):
    if x <=1:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
    
for i in range(5):
    print(fibonacci(i))