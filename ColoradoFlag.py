# Assignment: HW13
# File: ColoradoFlag.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date: April 18, 2025
# Description of Program: Draw the Colorado state flag using turtle graphics
# in a modular and scalable way. 

# Import necessary libraries 
import turtle
import math

# Define RGB colors based on official Colorado flag palette
myBlue = (0, 33, 71)
myRed = (191, 10, 48)
myGold = (255, 221, 0)
myWhite = (255, 255, 255)

# Set up the drawing window
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.colormode(255)
screen.bgcolor(myWhite)

# Create turtle for drawing
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw a filled rectangle at (x, y) with given width, height, and color
def drawRectangle(turtleObj, x, y, width, height, color):
    turtleObj.penup()
    turtleObj.goto(x, y)
    turtleObj.setheading(0)
    turtleObj.fillcolor(color)
    turtleObj.begin_fill()
    for _ in range(2):
        turtleObj.forward(width)
        turtleObj.right(90)
        turtleObj.forward(height)
        turtleObj.right(90)
    turtleObj.end_fill()

# Draw a filled circle centered at (centerX, centerY) with specified radius and color
def drawCircle(turtleObj, centerX, centerY, radius, color):
    turtleObj.penup()
    turtleObj.goto(centerX, centerY - radius)
    turtleObj.setheading(0)
    turtleObj.fillcolor(color)
    turtleObj.begin_fill()
    turtleObj.circle(radius)
    turtleObj.end_fill()

# Draw a filled triangle using three vertices and a given color
def drawTriangle(turtleObj, x1, y1, x2, y2, x3, y3, color):
    turtleObj.penup()
    turtleObj.goto(x1, y1)
    turtleObj.fillcolor(color)
    turtleObj.begin_fill()
    turtleObj.goto(x2, y2)
    turtleObj.goto(x3, y3)
    turtleObj.goto(x1, y1)
    turtleObj.end_fill()

# Draw the full Colorado state flag
def drawColoradoFlag():
    # Define flag dimensions
    flag_width = 600
    flag_height = 400
    stripe_height = flag_height / 3

    # Draw the top blue stripe
    drawRectangle(t, -300, 200, flag_width, stripe_height, myBlue)
    # Middle white stripe is the background color (no drawing needed)
    # Draw the bottom blue stripe
    drawRectangle(t, -300, 200 - 2 * stripe_height, flag_width, stripe_height, myBlue)

    # Draw the red "C" as a large circle
    drawCircle(t, -75, 0, 100, myRed)

    # Draw the white triangular notch inside the "C"
    angle_rad = math.radians(60)
    arm_length = 130
    x1, y1 = -75, 0
    x2 = x1 + arm_length * math.cos(angle_rad / 2)
    y2 = y1 + arm_length * math.sin(angle_rad / 2)
    x3 = x1 + arm_length * math.cos(angle_rad / 2)
    y3 = y1 - arm_length * math.sin(angle_rad / 2)
    drawTriangle(t, x1, y1, x2, y2, x3, y3, myWhite)

    # Draw the inner gold circle centered within the "C"
    drawCircle(t, -75, 0, 50, myGold)

# Main function to execute flag drawing
def main():
    drawColoradoFlag()
    turtle.done()

# Run main function
main()
