def equl(x,y,z):
    a =compareMax(x,y)
    m = compareMax(a,z)
    return m
    
    
    
def compareMax(x,y):
    if x>y:
        return x
    else:
        return y
    
max=equl(10,15,14)
print(max)