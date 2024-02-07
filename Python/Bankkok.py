#Process

#data
account = {"User1":5000,"User2":7000,"User3":1000,"User4":3000}

def getBalance():
    print("Balance:",account)
    
def deposite(money):
    if not type(money) is int and not type(money) is float:
         raise Exception("Input Number")
    print("Deposite:",money)
    account["User1"]+=money
    
def withDraw(money):
    if not type(money) is int and not type(money) is float:
         raise Exception("Input Number")
    if money < 0:
        raise Exception("You dont have money")
    if money > account["User1"]:
        raise Exception("You need have more money")
    print("Withdraw:",money)
    account["User1"]-=money   
    
def tranfer(money):
     if not type(money) is int and not type(money) is float:
         raise Exception("Input Number")
     if money < 0:
        raise Exception("You dont have money")
     if money > account["User1"]:
        raise Exception("You need have more money")
     print("Tranfer:",money)
     account["User1"]+=money
     account["User2"]-=money
    
    
    
try:  
    getBalance()
    deposite(2000)
    getBalance()
    withDraw(5000)
    getBalance()
except Exception as e:
    print(e)
    