
i=1
l=[]
while i<=100:
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        l.append(i)
    i+=1
print(l)


i=0
while i<=100:
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print(i,"prime")
    i+=1

def num():
    i=0
    l=[]
    while i<=n:
        count=0
        j=1
        while j<=i:
            if i%j==0:
              count+=1
            j+=1
        if count==2:
            l.append(i)
        i+=1
    print(l)
n=int(input("enter the number"))
num()

