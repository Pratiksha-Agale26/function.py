def perfect():
    i=1
    while i<=a:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum=sum+j
            j+=1
        i+=1
    if sum==a:
        print("perfect number")
    else:
        print("not perfect")
a=int(input("enter the number"))
perfect()

