my_list = [1,0, 5,0,0, 4, 6,-2, 8, 11,-4, 3, 12]

new_list = list(filter(lambda x: (x!=0), my_list))

print(new_list)

my_list = [2,"pratiksha",4,"agale",12,"shruti"]

new_list = list(filter(lambda x: x%2 , my_list))

print(new_list)

num=lambda x:x/6
print(num(12))


a=[1,2,3,4,5,6,7,8,9,10]
# a=[-1,2,-3,4,-5,6,-7,8,-9,10]
b=list(filter(lambda x:x%2==0,a))
print(b)