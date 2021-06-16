# Day 5 challenge

#1. write a program to create a list of n integer values and do the following

#add an item in to the list (using function)

#List declaration (List is mutable)
L=[10,20,30,40] 
print(L) #print the List

#or

for i in range(len(L)):
    print(L[i])
#add element using append method
L.append(50)
print(L)
#add sequence using extend method
K=[60,70,80,90,100]
L.extend(K)
print(L)
#insert an element at given index
index=int(input("enter the index:"))
item=int(input("enter the item to be insert:"))
L.insert(index, item)
print(L)

#Delete using function

#using del statement
del L[5]
print(L)
del L[3:6] #delete a particular slice
print(L)
# using pop method
element=L.pop() #last item
print(element)
ind=int(input("enter the index element need to be remove and extract:"))
element=L.pop(ind)
print(element)
#using remove method
L.remove(L[2])
print(L)
L.remove(80)
print(L)

#store the largest number from the list to a variable
L1=[78, 67, 45, 43, 86, 2, -1, 100, 34]
low=min(L1)
high=max(L1)
print(low)
print(high)
L1.sort()
print(L1[0])
print(L1[-1])
out=sorted(L1)
print(out)

# python tuples

#create the tuple and reverse it.
kamal_tuple=(20, 40, 30, 45, 65)
print(kamal_tuple[0:])
S=sorted(kamal_tuple)
print(S) # print the tuple 
rev=sorted(S, reverse=True)
print(rev) # print the tuple in reverse form

#create a tuple and convert tuple into list.
print()
tuple1=("kamal", 20, 175.50)
print("tuple is :", tuple1)
list12=list(tuple1)
print("Corresponding List is: ",list12)