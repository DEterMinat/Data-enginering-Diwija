money = int(input("Your money :"))

if money>=1000:
    print("1000 bath Count :",money//1000,"count")
    money %= 1000
if money>=500:
    print("500 bath count :",money//500,"count")
    money %=500
if money >= 100:
    print("100 bath count :",money//100,"count")
    money %=100
if money >= 50:
    print("50 bath count :",money//50,"count")
    money %=50
if money >= 20:
    print("20 bath count :",money//20,"count")
    money %=20    
