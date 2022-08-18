def ave():
    i=0
    sum=0
    while i<=3:
        a=int(input("enter the number"))
        sum+=a
        i+=1
    print(sum)
    print(sum/i)
ave()

def eligible(age):
    if age>=18:
        print("you are eligible")
    else:
        print("not eligible")
a=int(input("enter the number"))
eligible(a)

