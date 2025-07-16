thisset = {"apple", "banana", "cherry"}
print(thisset)

#Check if an item is present in the set
#using for loop with in keyword
for x in thisset:
  print(x)
  
#using only 'in' keyword
print("banana" in thisset)

#using not keyword
print("banana" not in thisset)



#Adding items in a set
thisset.add("orange")

print(thisset)




#Add items of one set to another
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#Adding items of a list to a set
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)




#Remove items in a set
thisset.remove("banana")
print(thisset)
        #OR
thisset.remove("banana")
print(thisset)
        #OR
x = thisset.pop()
print(x)
print(thisset)
        #OR
del tropical

print(tropical)


#make a set empty
thisset.clear()
print(thisset)



#Loop through the set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
  

#Joining two sets
#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# use of  |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


#joining multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


#join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


#Adding items of a set into another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#intersection of two sets__ join two sets but keep only duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


#keep only the items that exist in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)


#Difference__keep all items from set1 that are not in set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
        #OR
set3 = set1 - set2
print(set3)


#keep the items that are not in both sets
set1.difference_update(set2)

print(set1)

