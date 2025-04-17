# File: Project1.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
#
# Date Created: 02/28/2025
# Description of Program: This program generates and prints a formatted calendar for any given month of 2025

# Define constants for days of the week
SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

# Define constants for months
JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

# Function to return the name of the month given its number
def monthName(n):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[n - 1]

# Function to return the first day of the month in 2025
def firstDayOfMonth(n):
    first_days = [WED, SAT, SAT, TUE, THU, SUN, TUE, FRI, MON, WED, SAT, MON]
    return first_days[n - 1]

# Function to return the number of days in a given month of 2025
def daysInMonth2025(n):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_months[n - 1]

# Function to print the calendar for a given month in 2025
def printCalendarMonth(n):
    # Print a blank line and the month title centered
    print()
    title = monthName(n) + ", 2025"
    header = "Su Mo Tu We Th Fr Sa"  # Header for days of the week
    total_width = len(header)
    num_leading_spaces = (total_width - len(title)) // 2
    print(" " * num_leading_spaces + title)  # Center the title
    print(header)

    start = firstDayOfMonth(n)  # Get the starting day of the month
    days = daysInMonth2025(n)   # Get the total days in the month

    # Print leading spaces for the first row based on the starting day
    print("   " * start, end="")    
    col = start  # Track the current column position

    # Loop through all days and print them in a calendar format
    day = 1
    while day <= days:
        # Print the day with proper spacing
        if day < 10:
            print(" " + str(day) + " ", end="")  # Add extra space for single-digit days
        else:
            print(str(day) + " ", end="")  # Print double-digit days normally

        col += 1  # Move to the next column

        # If at the end of the week, print a new line
        if col == 7:
            print()
            col = 0  # Reset column count for a new week
        
        day += 1  # Move to the next day

    # Print a newline if the last row wasn't full
    if col != 0:
        print()
    print()

# Main function to interact with the user
def main():
    print("\nWelcome to our calendar utility!")
    print("Print the calendar for any month in 2025.")
    print()
    
    while True:
        # Prompt user for input
        user_input = input("Enter a month [1..12] or 0 to stop: ")
        
        # Validate user input: Ensure it is a number between 0 and 12
        if (user_input == "0" or user_input == "1" or user_input == "2" or 
        user_input == "3" or user_input == "4" or user_input == "5" or 
        user_input == "6" or user_input == "7" or user_input == "8" or 
        user_input == "9" or user_input == "10" or user_input == "11" or 
        user_input == "12"):
            month_num = int(user_input) # Convert to integer
        else:
            print("Month must be a number between 1 and 12, or 0 to stop. Try again.\n")
            continue # Ask again if input is invalid
        
        # If the user enters 0, exit the program        
        if month_num == 0:
            print("Thanks for visiting! Goodbye!")
            break
        
        # Print the calendar for the given month
        else:
            printCalendarMonth(month_num)

# Calls main function
main()