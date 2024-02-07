city = ["Diw","Jiw","God"]

def additon(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    print("Total:",total)
    
additon(1,2,3,4,5,6,7,8,9,10)