def drive(a):
    if a<=70:
        print(a,"ok")
    elif a>70:
        n=a//15
        print(n,"points")
        if n>=12:
            print(n," license suspended")
a=int(input('enter the numbr'))
drive(a)