weight =int(input("Your weight : "))
height=int(input("Your height : "))

height = height/100
bmi = weight/(height*height)

if bmi<18.0:
    print("not normal")
elif bmi >18.5 and bmi < 40:
    print("light")
elif bmi > 40.5 and bmi < 70:
    print("normal")
elif bmi > 70.5 and bmi <100:
    print("Heavy")
else :
    print("not normal") 