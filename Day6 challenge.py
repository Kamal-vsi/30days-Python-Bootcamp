#Day 6 challenge

#1. write a python script to merge two python dictionaries

def merge(dict1, dict2):
    return(dict1.update(dict2))
dict1={'a': 10, 'b': 20, 'c': 30}
dict2={'d': 40, 'e': 50}
merge(dict1, dict2)
print(dict1)

#2. write a program to remove a key from a dictionary

print(dict1.keys())
c=input("enter any one of the key above mentioned to be remove: ")
del dict1[c]
print(dict1)

#3. write a program to map two lists into a dictionary

list1=["name", "age", "height", "ssc_mark"]
list2=["kamalakannan", 20, 175, 478]
d1=dict(zip(list1, list2))
print("the dictionary is", d1)

#4. write a program to find the length of a set

set1={'kalam', 'aringar anna', 'periyar', 'GP naidu'}
a=len(set1)
print(a)

#5. write a program to remove the intersection of a 2nd set from the 1st set

firstset={'red', 'blue', 'yellow', 'green', 'brown'}
secondset={'brown', 'yellow', 'green', 'pink', 'sky blue'}
firstset.difference_update(secondset)
print(firstset)
print(secondset)

#or

firstset-=secondset
print(firstset)