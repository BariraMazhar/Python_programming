fruit = input("Enter the name of one of three fruits; Banana, Apple, Mango:  ")
colour = input("What is the colour of the fruit right now ? (i.e, Banana: Green,Yellow,brown): ")

if(fruit == "Banana"):
    if(colour == "green"):
        state = "unripe"
    elif(colour == "yellow"):
        state = "ripe"
    else:
        state = "over ripe"
        
elif(fruit == "Apple"):
    if(colour == "green"):
        state = "unripe"
    elif(colour == "red "):
        state = "ripe"
    else:
        state = "over ripe"
        
else:
    if(colour == "green"):
        state = "unripe"
    elif(colour == "yellow"):
        state = "ripe"
    else:
        state = "over ripe"
    
print("your fruit is " + state)