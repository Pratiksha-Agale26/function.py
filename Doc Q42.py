a=[12, 67, 98, 34]
i=0
b=[]
while i<len(a):
    a[i]=str(a[i])
    j=0
    s=0
    while j<len(a[i]):
        s+=int(a[i][j])
        j+=1
    b.append(s)
    i+=1
print(b)