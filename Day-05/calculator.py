# Calculator code using

import sys

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])


def addition(num1, num2):
    sum = num1 + num2
    return sum

def subtraction(num1, num2):
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

def divide(num1, num2):
    div = num1 / num2
    return div

if operation == 'add':
    result = addition(num1, num2)
elif operation == 'sub':
    result = subtraction(num1, num2)
elif operation == 'mul':
    result = multiplication(num1, num2)
elif operation == 'div':
    result = divide(num1, num2)
else:
    result = "Invalid operation selection!!" 

print(result)