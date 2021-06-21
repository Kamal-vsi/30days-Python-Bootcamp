#Day8 challenge
#1. write a python program to merge two dictionaries
def merge(dict1,dict2):
    dict1.update(dict2)
dict1={"name1": "kamal", "age":20, "height":175.00}
dict2={"mothername": "Bharathi", "fathername": "kathavarayan"}
merge(dict1, dict2)
print(dict1)

#2. sort values from descending to ascending in list and converted to set
list1=[30, 40, 20, -1, 150]
list2=sorted(list1)
print(type(list1))
list1.sort(reverse=True)
print(list1)
set1=set(list1)
print(type(set1))
print(set1)

#3. sort the list as the value of dictionary
# using function
dict1={'kamal': [3,2,1,6], 'kannan': [7,6,8,3], 'shiva': [80, 90, 99, 56, 75]}
print(sorted(dict1))
def func(dict2):
    res=dict()
    for key in sorted(dict1):
        res[key]=sorted(dict1[key])
    return res
print("the sorted list as value in dictionary", func(dict1))

# without using function
def func1(dict2):
    for key in sorted(dict1):
        list2=dict1[key]
        for i in range(len(list2)):
            for j in range(len(list2)):
                if(list2[i]<list2[j]):
                    temp=list2[i]
                    list2[i]=list2[j]
                    list2[j]=temp
        dict1[key]=list2
    return dict1    
print("the sorted list as value in dictionary  without using function:",func1(dict1))

#4. change the first occurence of the character to a user specified input of a given string
str1=input("Enter the string: ")
str2=input("enter the certain string to be replaced:")
str3=input("enter the replacing string:")
print(str1.replace(str2, str3, 1))

#5. change the first occurence of character from string into capital letter
str1=input("enter the first string: ")
str2=input("enter the second string:")
print(str1.capitalize()+","+str2.capitalize())

#6. find the repeated items in a list
list1=[1,2,3,3,3,2,0,9,8,7,5,7,8,4,3,6,5,12,23,45]
list2=[]
for i in list1:
    if list1.count(i)>1:
        if i not in list2:
            list2.append(i)
print(list2)

#7. check the sum of three numbers are divided by the user defined input

a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
c=int(input("enter the num3:"))
sum=a+b+c
div=int(input("enter the number to divide the sum:"))
if(sum%div==0):
    print("The given number is a perfect divisor")
    print("the answer is:", sum/div)
else:
    print("The given number is not a perfect divisor")
    
#8. write a program to find mean, median, mode for three given number

a=[20, 30, 45, 6, 7, 8, 35, 40, 12, 12, 12, 12]
import statistics
print(statistics.mean(a))
print(statistics.median(a))
print(statistics.mode(a))

#9. swap two strings

a=input("enter the first string: ")
b=input("enter the second string: ")
print("before swaping "+a+','+b)
a,b=b,a
print("after swaping "+a+','+b)

#10. convert a number to binary and octal

num=int(input("Enter the number:"))
print("the binary form is:", bin(num))
print("the octal form is:", oct(num))