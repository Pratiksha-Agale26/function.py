a=["i am pratiksha"]
for i in a:
    x=i.split()
print(x)


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

x=lambda a,b:a+b
print(x(2,3))

def num():
    n=int(input("enter the number"))
    i=1
    count=0
    while n<=i:
        if n%i==0:
            count+=1
        i+=1
    if count==2:
        print("prime number")
    else:
        print("not")
num()

def num():
    i=0
    while i<=10:
        print(i)
        i+=1
        if i==5:
            break
num()