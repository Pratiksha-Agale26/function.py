def num():
    a=[[1],[1,3],[5,7],[9,11],[13,15,17]]
    i=0
    max_a=a[0]
    min_a=a[0]
    while i<len(a):
        if len(a[i])<len(min_a):
            min_a=a[i]
        if len(a[i])>len(max_a):
            max_a=a[i]
        i=i+1
    print(len(max_a),max_a)
    print(len(min_a),min_a)
num()


    