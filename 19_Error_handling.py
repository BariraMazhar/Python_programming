file = open('test.txt', 'w')


#  syntax #01
try:
    file.write('This is a test file.')
finally:
    file.close()
    
# syntax #02
with open('test.txt', 'w') as file:
    file.write('This is a test file')    