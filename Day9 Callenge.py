#Day9 challenge

#1. iterate the elements in the list and add 2 fpr each element:
list1=[10, 20, 30, 40, 50]
for i in range(len(list1)):
    list1[i]=list1[i]+2
print(list1)

#2. program to get certain pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()    

#3. program to print fibonnaci sequence
# to get the nth value of the fibonnaci sequence
def fibonacci(n):
    if n<=0:
        return
    elif n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the value: "))        
print(fibonacci(n))
#to print the fibonnaci sequence upto the nth value
def fibonacci1(n):
    n1, n2=0, 1
    count=0
    if n<=0:
        print("invalid output")
    elif n==1:
        print(n1)
    else:
        while count<n:
            print(n1, end=' ')
            next1=n1+n2
            n1=n2
            n2=next1
            count+=1
n=int(input("Enter the value to get fibonacci series:"))
fibonacci1(n)

#4. explain amstrong number and code the program

# Answer: Amstrong number is a number whose sum of the cube of its individual digit is equal to the same number

#program to check whether the given number is amstrong or not
print()
n=int(input("Enter the number:"))
temp=n
sum1=0
while temp>0:
    digit=temp%10
    sum1=sum1+(digit**3)
    temp=int(temp/10)
if(sum1==n):
    print("The given number is armstrong number")
else:
    print("The given number is not an armstrong number")

#5. write a program to print multiplication table of nine.
for i in range(1, 17):
    print("9 x",i,"=",i*9)

#6. check if the number is negative or positive
list2=[10, -20, 30, 40, -50, -2567]
for i in list2:
    if i>=0:
        print(i,"is positive")
    else:
        print(i,"is negative")

#7. program to convert no.of days to age:
def getage(n):
    return n//365
n=int(input("enter the no.of days:"))
print("The age is:",getage(n))

#8. Solve trignometry problem using math function write a program to solve using math function
import math
def trignometry(a, b):
    if(a=='sin'):
        print(math.sin(b))
    elif(a=='cos'):
        print(math.cos(b))
    elif a=='tan':
        print(math.tan(b))
    elif a=='cosin':
        print(1/math.sin(b))
    elif a=='sec':
        print(1/math.cos(b))
    elif a=='cot':
        print(1/math.tan(b))
a=input("Enter the trignometric term: ")
b=int(input("Enter the angle in deg:"))
trignometry(a, b)

#9.create a basic calculator using if condition only:
def calculator(a, b, c):
    if b=='+':
        print("the answer is",a+c)
    elif b=='-':
        print("the answer is",a-c)
    elif b=='*':
        print("the answer is",a*c)
    elif b=='/':
        print("the answer is",a/c)
    elif b=='//':
        print("the answer is",a//c)
    elif b=='**':
        print("the answer is",a**b)
    elif b=='%':
        print("the answer is",a%b)
n1=int(input("Enter the first number:"))
sign=input("Enter the operation to be done: + for addition, - for subtraction, * for multiplication, / for division, // for floor divison(to get quotient), % for modulo(to get remainder), ** for exponential:")
n2=int(input("Enter the second number:"))
calculator(n1, sign, n2)