#numeric types
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#text type
#String
print("Hello")
print('Hello')

#Boolean type
print(10 > 9)
print(10 == 9)
print(10 < 9)

#collection types
#Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])

#tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
thistuple[2] = "mango"
print(thistuple)

#dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

#set
thisset = {"apple", "banana", "cherry"}
print(thisset)


