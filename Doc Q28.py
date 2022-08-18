def function(num):
    i=0
    while i<=num:
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
        i+=1
num=int(input("enter the number"))
function(num)