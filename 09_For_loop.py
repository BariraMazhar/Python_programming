#for a string
name="johnny"
for i in name:
    print(i)


#for a list
cars=['audi','BMW','dodge','supra','bugatti']
for name in cars:
    print( "car name is",name)
    for i in name:
        print(i)
    print("number=",len(name))

#using range() in for loop
   #with stop only
    for i in range(5):
        print(i)      #numbers from 0 to 4 will be printed

   #with start and stop
    for i in range(3,12):
        print(i)      #numbers from 3 to 11 will be printed

   #with start, stop and step
    for i in range(3,30,3):
        print(i)       #numbers from 3 to 29 with a gap of 3 will be printed