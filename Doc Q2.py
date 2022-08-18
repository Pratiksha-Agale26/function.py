def max():
    if num>num1 and num>num2:
        print(num,"is maximum")
    elif num1>num and num1>num2:
        print(num1,"is maximum")
    elif num2>num and num2>num1:
        print(num2,"is maxmum")
    else:
        print(num,"is not maximum")
num=int(input("enter the number"))
num1=int(input("enter the number"))
num2=int(input("enter the number"))
max()

