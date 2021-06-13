# Day 2 Challenge

#How to print a string?
print('30 days 30 hour challenge')
print("30 days 30 hour challenge")

#Assigning string to variables
Hours = "thirty"
print(Hours) #output is thirty
name = 'K.Kamalakannan'
print(name) #output is K.Kamalakannan

#indexing using string
Days="Thirty days"
print(Days[0]) #output is T
print(Days[10]) #output is s
print(Days[6]) #output is ' '(space)
print(Days[3]) #output is r

#How to print the particular character from certain text?
Challenge="I will win"
print(Challenge[7:10]) #output is win
name="K.Kamalakannan"
print(name[2:7]) #output is Kamal

#Length of the character
Challenge="I will win"
print(len(Challenge)) #output is 10
name="K.Kamalakannan"
print(len(name)) #output is 14

#Convert string to lower character
Challenge="I will win"
print(Challenge.lower()) #output is i will win 
print(Challenge.upper()) #output is I WILL WIN

#String concatenation- joining two strings
a="30 days"
b="30 hours"
c=a+b
print(c) #output is 30 days30 hours
a="kamala"
b="kannan"
c=a+b
print(c) #output is Kamalakannan

#Adding space during concatenation
a="30 days"
b="30 hours"
c=a+" "+b
print(c) #output is 30 days 30 hours

#casefold() usasge
text="Thirty days Thirty hours"
x=text.casefold()
print(x) #output is thirty days thirty hours
y=text.capitalize()
print(y) #output is Thirty days thirty hours

text1="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
z=text1.capitalize()
print(z) #output is Don't trouble trouble until trouble troubles you.
w=text1.isalpha()
print(w) #output is False
v=text1.isalnum()
print(v) #output is False

text2='a'
x=text2.isalpha()
print(x) #output is True
num1="1234"
y=num1.isalnum()
print(y) #output is True
num2="1234abcd"
z=num2.isalpha()
v=num2.isalnum()
print(z) #output is False
print(v) #output is True