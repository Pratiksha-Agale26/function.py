def chr():
    a='The quick Brow Fox'
    i=0
    count=0
    counter=0
    while i<len(a):
        if a[i]>="A" and a[i]<="Z":
            count+=1
        elif a[i]>="a" and a[i]<="z":
            counter+=1
        i+=1
    print("upper",count)
    print("lower",counter)
chr()


