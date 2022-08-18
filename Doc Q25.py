def number():
    a=int(input("enter the number"))
    if a%3==0:
        print("fizz")
    elif a%5==0:
        print("Buzz")
    elif a%3==0 and a%5==0:
        print("fizzBuzz")
    else:
        print("not")
number()