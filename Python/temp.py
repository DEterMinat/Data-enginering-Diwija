temp = int(input("Temp :"))
degree = temp[:-1].upper()
unit = temp[:-1].upper()

print(degree," = ",unit)
if unit =="C":
    result = (9*degree)/5+32
if unit =="F":
    result = (degree - 32)*5/9
    
print(result)