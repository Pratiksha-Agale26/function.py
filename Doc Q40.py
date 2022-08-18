


number=str(input("Enter the number :"))
def num(number):
    digits = list(number)
    for j in digits:
        print(int(j)**2,end="")
num(number)
