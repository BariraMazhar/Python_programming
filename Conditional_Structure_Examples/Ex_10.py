speccie = input("Enter animal specie: ")
age = int(input("Enter age of your pet: "))

if(speccie == 'dog'):
    if(age < 2):
        print("puppy food is best suited for your pet.")
    else:
        print("no recommended food")

elif(speccie == 'cat'):
    if(age > 5):
        print("senior cat food is best suited for your pet")
    else:
        print("no recommended food")
        
else:
        print("no recommended food foor your pet")