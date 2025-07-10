marks = int(input("Enter your marks: "))

if(marks >= 101):
    print("Please enter correct marks within 1-100")
    exit()

if(marks >=90 ):
    grade = 'A'
elif(marks >= 80):
    grade = 'B'
elif(marks >= 70):
    grade = 'C'
elif(marks >= 60):
    grade = 'D'
else:
    grade = 'F'
    
print("your grade is " + grade)
