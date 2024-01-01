

# #If-else statement
age=int(input("Enter your age: "))
print("your age is ",age)
if(age>18):
   print("you can drive")
else:
   print("you can't drive")


#elif (If-elseIf) statement
num=int(input("Enter a number: "))
if (num>0):
	print("number is positive")
elif (num<0):
	print("number is negative")
else:
	print("The number is zero")
        


#nested if statement
num=int(input("Enter a number: "))
if (num==0):
	print("The number is zero")
elif(num>0):
	if (num<=10):
		print("number is between 1-10")
else:
    print("number is negative")
	             
        
	