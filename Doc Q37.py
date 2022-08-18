def number():
    a=[True, True, True, False,True, True, True, True ,True, False, True, False,True, False, False, True ,True, True, True, True ,False, False, True, True]
    i=0
    sum=0
    while i<len(a):
        sum+=a[i]
        i+=1
    print(sum)
number()