def remove():
    a=[1450,960000,1050,-1050]
    i=0
    b=[]
    while i<len(a):
        while a[i]>0:
            if a[i]%10!=0:
                b.append(a[i])
                break
            a[i]//=10
        i+=1
    print(b)
remove()
