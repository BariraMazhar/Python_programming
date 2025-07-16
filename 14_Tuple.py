#Tuples can have same value multiple times
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Length of tuple
print(len(thistuple))


#Tuple with one item
thistuple2 = ("apple",)         #remember the comma at the end
print(type(thistuple2))


#creating tuple using tuple constructor
thistuple3 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple3)


#Tuples can be accessed using same methods as lists


#Changing, Adding, Removing
#Tuples are unchangeable so to change the tuple items , the tuple is converted into a list, the item is changed and list is again converted into tuple again.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Like changing, items in a tuple are added and removed in the same way.



#delete whole tuple
del thistuple
print(thistuple)


#Unpacking the tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple.In Python, we are also allowed to extract the values back into variables. This is called "unpacking"
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Assign the value as a list
#1
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#2
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)




#Loop through a tuple
#we can loop through aa tuple like a list



#Joining two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#Multiply the tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

