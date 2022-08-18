def check_number():
    list=[2,-7,5,-64,-12]
    i=0
    count=0
    counter=0
    while i<len(list):
        if (list[i])>0:
            count+=1
        else:
            counter+=1
        i+=1
    print("positive",count)
    print("negative",counter)
check_number()

def check_number():
    a=[2,-7,5,-64,-12]
    i=0
    b=[]
    while i<len(a):
        if a[i]>0:
            b.append(1)
        else:
            b.append(0)
        i+=1
    print(b)
check_number()