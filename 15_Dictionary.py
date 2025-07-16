thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#duplicate values in a dictionary will overwrrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)



#length of dictionary
print(len(thisdict))


#type of dictionary
print(type(thisdict))



#creating dictionary using dict() constructor
thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)



#Accessing items in dictionary
x = thisdict["model"]
        #OR
x = thisdict.get("model")



#get a list of values 
x = thisdict.values()



#changing items in dictionary
thisdict["year"] = 2020
print(x) 
        #OR
thisdict.update({"year": 2020})




#Adding item in dictionary
thisdict["color"] = "red"
print(x)
        #OR
thisdict.update({"color": "red"})



#Removing items
thisdict.pop("model")
print(thisdict)
        #OR
thisdict.popitem()
print(thisdict)
        #OR
del thisdict["model"]
print(thisdict)



#get a list of items of the dictionary
x = thisdict.items()



#Check if a key exists in a dictionary
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



#Empty the Dictionary
thisdict.clear()
print(thisdict)




#Loop through the dictionary
#print items
for x in thisdict:
  print(x)
  
#print values
for x in thisdict:
  print(thisdict[x])
  
#loop through the values
for x in thisdict.values():
  print(x)
  
#loop through the Keys
for x in thisdict.keys():
  print(x)

#Loop through both keys and values
for x in thisdict.items():
  print(x)



#Copying a dictionary
mydict = thisdict.copy()
print(mydict)
        #OR
mydict = dict(thisdict)
print(mydict)



#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Abdullah",
    "year" : 2004
  },
  "child2" : {
    "name" : "Ahmad",
    "year" : 2007
  },
  "child3" : {
    "name" : "Adan",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])



#Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])