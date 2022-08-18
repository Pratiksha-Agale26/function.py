# def num():
#     a=[2,1,3,3,1,8]
#     i=0
#     b=[]
#     while i<len(a):
#         if(a[i]) not in b:
#             b.append(a[i])
#         i+=1
#     print(b)
# num()

# def num():
#     a=[30,15,45,3,1,8]
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i]%5==0:
#             b.append(a[i])
#         i+=1
#     print(b)
# num()

# def fact(num):
#     if num==1:
#         return 1
#     return num*fact(num-1)
# print(fact(5))

def add(a,b):
    c=a+b
    print(c)
    def name(t,k):
        print(t,k)
    name("tanu","khose")
add(5,6)

def num():
    a=[[4,5],[3,6]]
    i=0
    sum=0
    while i<len(a):
        j=0
        s=0
        while j<len(a[i]):
            sum+=(a[i][j])
            j+=1
        sum+=s
        i+=1
    print(sum)
num()

def num():
    b=int(input('enter the number'))
    a=[1,5,6,7,8,3,4]
    i=0
    # count=0
    c=[]
    while i<len(a):
        if b<(a[i]):
            c.append(a[i])
        i+=1
    print(c)
num()

def num():
    a=["123abc"]
    i=0
    while i<len(a):
        # i+=1
        print(a[-i],end=" ")
        i+=1
num()
        
def reverse():
    a=["1234abcd"]
    i=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            j+=1
        i+=1
        print(a[-i][-1],end="")
reverse()

def num():
    i=0
    while i<=100:
        print(i)
        i+=1
num()

def num():
    i=100
    while i>=1:
        print(i)
        i-=1
num()

