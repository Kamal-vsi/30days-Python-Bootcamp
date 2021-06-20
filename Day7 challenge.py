#1. create a function getting two integer inputs from user & print the following
def math_funcs(num1, num2, sign):
    if(sign=='+'):
        print("Addition of two numbers :", num1+num2)
    elif(sign=='-'):
        print("Subtraction of two numbers :", num1-num2)
    elif(sign=='*'):
        print("Multiplication of two numbers :", num1*num2)
    elif(sign=='/'):
        print("Division of two numbers :", num1/num2)
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
sign=input("enter the mathematical sign + for addition, - for subtraction, * for multiplication, / for division:")
math_funcs(a, b, sign)

print()
#2. Create a function covid() & it should accept patient's name and body temperature. By default the body temperature is 98 deg
def covid(name1, temp="98 deg F"):
    print("The patient name is:", name)
    print("Patient's body temperature is:", temp)
name=input("Enter Patient name:")
covid(name)    