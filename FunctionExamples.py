# File: FunctionExamples.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course: CS303E
#
# Date: 02/22/2025
# Description of Program: This program is designed to implement various functions that perform different actions.

import math

def sum3Numbers(x, y, z):
    return x + y + z

def multiply3Numbers(x, y, z):
    return x * y * z

def sumUpTo3Numbers(x, y=0, z=0):
    return x + y + z

def multiplyUpTo3Numbers(x, y=1, z=1):
    return x * y * z

def printInOrder(x, y):
    if x <= y:
        print(x, y)
    else:
        print(y, x)

def areaOfSquare(side):
    if side < 0:
        print("Negative value entered")
    else:
        return side * side

def perimeterOfSquare(side):
    if side < 0:
        print("Negative value entered")
    else:
        return 4 * side
    
def diagonalOfRectangle(h, w):
    if h < 0 or w < 0:
        print("Negative value entered")
        return None
    return (h**2 + w**2) ** 0.5
    
def areaOfCircle(radius):
    if radius < 0:
        print("Negative value entered")
    else:
        return math.pi * radius * radius

def circumferenceOfCircle(radius):
    if radius < 0:
        print("Negative value entered")
    else:
        return 2 * math.pi * radius

def bothFactors(d1, d2, x):
    return x % d1 == 0 and x % d2 == 0

def squareAndCircle(x):
    print("\nCircle with radius", x, "has:")
    print("   Area:", areaOfCircle(x))
    print("   Circumference:", circumferenceOfCircle(x))
    print("Square with side", x, "has:")
    print("   Area:", areaOfSquare(x))
    print("   Perimeter:", perimeterOfSquare(x))

def factorial(n):
    if n < 0:
        print("Input must be positive.")
        return None
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

def numberLength(n):
    return len(str(n))

def sumPositiveNumbers():
    sum = 0
    while True:
        number = float(input("Enter a number: "))
        if number == 0:
            return 0
            break
        elif number < 0:
            print("Illegal input.")
            continue
        sum += number
    return sum