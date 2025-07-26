#square of a number
def square(num):
    return num ** 2


print(square(6))


#sum of two numbers
def sum(para1, para2):
    return para1 + para2

print(sum(3, 9))




#Multiply two numbers
def multiply(a, b):
    return a * b


print(multiply(2, 5))
print(multiply(3, 'x'))




#carea and circumference of a circle
import math

def circle(radius):
    area = 2 * math.pi *radius
    circumference = 2 * math.pi * radius
    return area, circumference


a, c = circle(6)
print(f"Area: {a}, Circumference: {c}")




#greet a person of given name
def greeting(name = 'John'):
    print(f"Hi ! {name}")

greeting('Alice')
greeting()




#lambda function
cube = lambda num: num ** 3

print(cube(6))




#function that takes variable number of arguments
def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_all(2, 4, 7, 8, 2, 9))



#function that takes named arguments
def print_kwargs(**kwargs):
    for key, value in  kwargs.items():
        print(f"{key}, {value}")
        

print_kwargs(name = "Alice", power = "magic")
print_kwargs(name = "Alice")
print_kwargs(name = "Alice", power = "magic", enemy = "cruela")




#even generator
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
        

# print(even_generator(10))
for num in even_generator(10):
    print(num)



