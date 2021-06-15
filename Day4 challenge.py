#1. Create three variables (a, b, c) to same value of any integer
a=b=c=50
print(a, b, c) #output is 50 50 50
print(a/10) #output is 5.0
print(b*50) #output is 2500
print(c+60) #output is 110

#2. Create a string variable of 5 chaaracters and replace the 3rd character with 'G'
name="abcde"
name1=name.replace('c', 'G')
print(name1) #output is abGde

#or using index position
y=input("enter the string:") # good morning
index=int(input("enter the index position to be replace:")) # 5
new_var=input("enter the replacing character:") # B
y=y[0:index]+new_var+y[index+1:]
print(y) #output is good Borning

#3. Create two values (a,b) of int, float data type & convert the vise versa, Hint: Convert a from int to float datatype
#& b from float to int datatype
a=20
b=32.40
print(type(a)) #output is <class 'int'>
print(type(b)) #output is <class 'float'>
a=float(a) #typecasted to float
b=int(b) #typecasted to int
print(a) #output is 20.0
print(type(a)) #output is <class 'float'>
print(b) #output is 32
print(type(b)) #output is <class 'int'>