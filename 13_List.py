# List
l1 = [3, 7, 9, 11]
#length of list
print(len(l1))

#type of list
print(type(l1))

#Access List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])

#negative indexing
print(thislist[-1])     

#Range of Indexes
print(thislist[2:5])        #list from 2nd index to 4th index is returned (excluding end points of range)

print(thislist[:4])         #returns the items from the beginning to index 3

print(thislist[2:])         #returns the items from index 2 to the end

#Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#Change Item Value
thislist[1] = "guava"
print(thislist)

#Add items in list by replacing
thislist2 = ["apple", "banana", "cherry"]
thislist2[1:2] = ["mango", "watermelon"]
print(thislist2)

#Insert Items
thislist2.insert(1, "orange")    #insert at the specified index
print(thislist2)

#append another list in a list
tropical = ["mango", "pineapple", "papaya"]
thislist2.extend(tropical)

#Add elements of a tuple to a list
thistuple = ("kiwi", "orange")
thislist2.extend(thistuple)
print(thislist2)

#remove items from list
thislist2.remove("banana")
print(thislist2)

#remove last item
thislist2.pop()
print(thislist2)

#remove at specific index
thislist2.pop(1)
print(thislist2)
del thislist2[0]
print(thislist2)

del thislist2         #del keyword also delete complete list

thislist.clear()        #clear keyword empties the list. 
print(thislist)


#loop through the list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
#loop using range of total length of list
for i in range(len(thislist)):
  print(thislist[i])
  

#loop using list comprehension
[print(x) for x in thislist]


#copy the list
# 1- using copy keyword
mylist = thislist.copy()
print(mylist)
# 1- using slice operator
mylist = thislist[:]
print(mylist)
# 1- using list method
mylist = list(thislist)
print(mylist)

#sort the list
thislist2 = [3,8,6,44,1,9]
thislist2.sort()