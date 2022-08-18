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