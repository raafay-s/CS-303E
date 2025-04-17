# Assignment: HW5
# File: MinMax.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date: 02/15/2025
# Description of Program: This program accepts user inputs and from it determines the count, minimum, and maximum values
    
def main():
    print()
    
    # Initializes count and min/max values
    count = 0
    min_val = 0
    max_val = 0
    
    while True:
        # Prompts user for input
        num = int(input("Enter an integer or -9999 to end: "))
        
        # Checks for sentinel value to exit loop
        if num == -9999:
            break
        
        # Sets min and max values for the first valid input
        if count == 0:
            min_val = num
            max_val = num
            
        else:
        # Updates min and max values accordingly
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        count += 1
    
    # Blank line
    print()
    
    # Displays results based on user input count
    if count == 0:
        print("You didn't enter any numbers.\n")
    else:
        print("You entered", count, "number" + ("" if count == 1 else "s") + ".")
        print("The maximum is", max_val)
        print("The minimum is", min_val, "\n")

# Calls main function
main()