number = [10,20,30,40,50]
name = ["Diw","Wave","Bank"]
name.append("Win")
name.insert(2,"God")
del name[3]
name.clear()
print(name)
number.remove(50)
number.pop()
print(number)
if 20 in number:
    print("Have")
else:
    print("No have")