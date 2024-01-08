a=input("Enter first number: ")
b=input("Enter second number: ")
x=input("Enter an operator: ")
match x:
 case '+':
  print(int(a)+int(b))
 case '-':
  print(int(a)-int(b))
 case '*':
  print(int(a)*int(b))
 case '/':
  print(int(a)/int(b))