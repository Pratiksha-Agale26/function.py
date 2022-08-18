def calculate_sum(a,b):
    sum = a+b
    print(sum)
calculate_sum(4,5)

def multiply(a,b):
    multiply=a*b
    return multiply
print(multiply(3,4))


def Avg(number1,number2,number3):
    sum=number1+number2+number3/3
    print(sum)
Avg(1,3,2)

def voter(age):
    if age > 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)

def distance(kms,meter):
    if kms < 20:
        print("close")
    elif meter < 50:
        print("median")
    else:
        print("far")
distance(20,30)

def function(num):
    return num+25
function(5)
print(num)