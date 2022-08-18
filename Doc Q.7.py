def fun():
    a=int(input("enter the weight"))
    b=int(input("enter the hight"))
    bmi=a/b
    if bmi<=18.5:
        print("underweight")
    if bmi<=18.5 and bmi>=25.0:
        print("normal")
    if bmi<=25.0 and bmi>=30.0:
        print("overwight")
    if bmi>30:
        print("obese")
fun()