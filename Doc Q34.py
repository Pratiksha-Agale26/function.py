def num():
    a=[23,12,11,10,8]
    # b=[12,45,23,2,24]
    max1=0
    max2=0
    i=0
    sum=0
    while i<len(a):
        j=0
        while j<len(a):
            if a[j]>max1:
                max1=a[j]
            if a[j]>max2 and a[j]!=max1:
                max2=a[j]
                sum+=a[j]+a[i]
            j+=1
        i+=1
    print(max1,"+",max2,"=",sum)
    # print(max2,sum)
num()



