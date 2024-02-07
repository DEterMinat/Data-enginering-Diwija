try:
    fw = open("score.txt","w",encoding="utf-8")
    for i in range(2):
        name=input("Enter your text :")
        fw.writelines(name+"\n")
    fw.close()    
    
except FileNotFoundError:
    print("File Not Found")