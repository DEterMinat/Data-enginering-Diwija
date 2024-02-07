while True:
    try:
        number1 =int(input("Number:"))
        number2 =int(input("Number:"))
        if number1 == 0 and number2 == 0:
            break
        if number1<0:
            raise Exception("Cant input them")
        result = number1/number2
        print(result)
        
    except Exception as e:
        print(e)
    finally:
        print("Do")