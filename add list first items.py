a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
b=[]
while i<len(a):
    j=0
    s=0
    c=[]
    while j<len(a[i]):
        s=a[j][i]
        c.append(s)
        j+=1
    b.append(c)
    i+=1
print(b)