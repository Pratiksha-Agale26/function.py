def sum():
    print(12+13)
sum()

def welcome():
    print("Welcome to function")
welcome()

isEven=12
def isEven():
    if(12%2==0):
        print("Even Number")
    else:
        print("Odd Number")
isEven()

def greet(*names):
    for name in names:
        print("Welcome"+name)
greet("Rinki", "Vishal", "Kartik", "Bijender")

def info (name, age ):
   print(name + " is " + age + " years old")

info("Sonu","17")
info("Sana", "17")
info("Umesh", "18")

def studentDetails(name,currentMilestone,mentorName):
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ",mentorName)
studentDetails("Nilam","loop","pratiksha")

def function_print_line():
    print("my name is rishabh")
    print("i am the co-founder of navgurukul")
function_print_line()


numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
print (max(numbers_list))