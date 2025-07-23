def square(num):
    return num ** 2


print(square(6))



def sum(para1, para2):
    return para1 + para2

print(sum(3, 9))





def multiply(a, b):
    return a * b


print(multiply(2, 5))
print(multiply(3, 'x'))





import math

def circle(radius):
    area = 2 * math.pi *radius
    circumference = 2 * math.pi * radius
    return area, circumference


a, c = circle(6)
print(f"Area: {a}, Circumference: {c}")




def greeting(name = 'John'):
    print(f"Hi ! {name}")

greeting('Alice')
greeting()




#lambda function
# 
cube = lambda num: num ** 3

print(cube(6))




#function that takes variable number of arguments
def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_all(2, 4, 7,8,2,9))