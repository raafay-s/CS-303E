# Assignment: HW7
# File: CalculatePi.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date Created: 03/03/2025
# Description of Program: The program estimates the value of π using two different mathematical approaches.
    
import math
import random

# Function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Circle class representing a circle with radius and center
class Circle:
    def __init__(self, rad, x, y):
        self.radius = rad
        self.center_x = x
        self.center_y = y
    
    def __str__(self):
        return "Circle of radius " + str(self.radius) + " centered at point (" + str(self.center_x) + ", " + str(self.center_y) + ")"
    
    def getRadius(self):
        return self.radius
    
    def getCenterX(self):
        return self.center_x
    
    def getCenterY(self):
        return self.center_y
    
    def getArea(self):
        return math.pi * (self.radius ** 2)
    
    # Check if a point (a, b) is inside the circle
    def pointInCircle(self, a, b):
        return distance(a, b, self.center_x, self.center_y) < self.radius

# Square class representing a square with a given side length and upper-left corner
class Square:
    def __init__(self, side, x, y):
        self.side = side
        self.upper_left_x = x
        self.upper_left_y = y
    
    def __str__(self):
        return "Square of side " + str(self.side) + " with upper left point at (" + str(self.upper_left_x) + ", " + str(self.upper_left_y) + ")"
    
    def getSide(self):
        return self.side
    
    def getULX(self):
        return self.upper_left_x
    
    def getULY(self):
        return self.upper_left_y
    
    def getArea(self):
        return self.side ** 2
    
    # Check if a point (a, b) is inside the square
    def pointInSquare(self, a, b):
        return (self.upper_left_x <= a < self.upper_left_x + self.side and
                self.upper_left_y - self.side < b <= self.upper_left_y)

# Function to estimate the value of Pi using Monte Carlo method
def estimatePi(c, n):
    hits = 0
    for _ in range(n):
        x = (random.random() * 2) - 1  # Generate random x in range [-1, 1]
        y = (random.random() * 2) - 1  # Generate random y in range [-1, 1]
        if c.pointInCircle(x, y):
            hits += 1
    return (hits / n) * 4  # Estimate of Pi

# Main function to run the simulation
def main():
    c = Circle(1, 0, 0)  # Define the unit circle centered at (0,0)
    s = Square(2, -1, 1)  # Define the square that inscribes the circle
    
    # Loop over different numbers of dart throws
    for n in [100, 1000, 10000, 100000, 1000000, 10000000]:
        calculated_pi = estimatePi(c, n)  # Estimate Pi using Monte Carlo method
        diff = calculated_pi - math.pi  # Calculate difference from actual Pi value
        
        # Print formatted results for each iteration
        print("n =", format(n, "<8"), "Calculated PI =", format(calculated_pi, "<10.6f"), "Difference =", format(diff, "+.6f"))

# Call main function
main()