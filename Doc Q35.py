def children():
    a=int(input('enter the number'))
    if a<14:
        print("drink toddy")
    elif a<18:
        print("drink coke")
    elif a<21:
        print("drink beer")
    elif a>=21:
        print("drink whisky")
    else:
        print("no drink")
children()

def num(a,b):
    c=a+b
    if c>=15 and c<=20:
        return 20
    else:
        return c
print(num(12,33))

def num():
    a=["abc","1212","dcad"]
    i=0
    while i<len(a):
        j=0
        count=0
        while j<len(a[i]):
            if len( a[i])==[-1]:
                count+=1
            j+=1
        i+=1
    print(count)
num()