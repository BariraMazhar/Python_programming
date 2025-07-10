password = input("Enter your password: ")
size = len(password)

if(size <= 6):
    print("Weak Password")
elif(size <= 10):
    print("Medium strength password")
else:
    print("Strong password !")