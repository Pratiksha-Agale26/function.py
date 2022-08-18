# def add_number(number1,number2):
#     print(number1+number2)
# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# add_number(num1,num2)

# def add_number_list( ):
#     a=[50,60,10]
#     b=[10,20,30]
#     i=0
#     sum=0
#     c=[]
#     while i<len(a):
#         j=0
#         while j<len(b):
#             sum=a[i]+b[i]
#             c.append(sum)
#             j+=1
#         i+=1
#     print(c)
# add_number_list( )

# def check_number(a,b ):
#     if a %2==0 and b%2==0:
#         print("both even number")
#     else:
        print("both numbers are not even")
check_number(12,16)
    
def check_numbers_list( ):
    a=[2, 6, 18, 10, 3]
    b=[6, 19, 24, 12, 75]
    i=0
    while i<len(a):
        j=0
        while j<len(b):
            if a[i]%2==0 and b[i]%2==0:
                print("both are even number")
            else:
                print("both are not even")
            j+=1
        i+=1      
check_numbers_list( )

