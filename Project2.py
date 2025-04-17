# Assignment: Project2
# File: Project2.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# Date: 04/07/2025
# Description of Program:
# This program provides various functionalities related to Fibonacci numbers. Users can generate a list of Fibonacci numbers, get the nth number, count how many are below a value, and more.

# Function to return the first n Fibonacci numbers
def firstNFibNumbers(n):    
    if n <= 0:
        return []  # Return empty list for non-positive input
    elif n == 1:
        return [0]  # Return first number
    elif n == 2:
        return [0, 1]  # Return first two numbers
    else:
        fib1, fib2 = 0, 1  # Initialize first two Fibonacci numbers
        fibs = [0, 1]  # List to store sequence
        for counter in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2  # Generate next number
            fibs.append(fib2)  # Add to list
        return fibs

# Function to return the nth Fibonacci number (0-based index)
def nthFibNumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib1, fib2 = 0, 1
    for _ in range(2, n + 1):
        fib1, fib2 = fib2, fib1 + fib2  # Update to next Fibonacci numbers
    return fib2

# Function to return all Fibonacci numbers less than or equal to a given number N
def fibsLessThanOrEqualTo(N):
    if N < 0:
        return []  # No Fibonacci numbers for negative input
    fibs = [0]  # Start with 0
    if N >= 1:
        fibs.extend([1, 1])  # Add first duplicate 1s
    fib1, fib2 = 1, 1
    while True:
        next_fib = fib1 + fib2  # Calculate next Fibonacci number
        if next_fib <= N:
            fibs.append(next_fib)  # Add it if within bounds
            fib1, fib2 = fib2, next_fib
        else:
            break  # Stop once next Fibonacci exceeds N
    return fibs

# Function to count how many Fibonacci numbers are less than or equal to N
def countFibsLessThanOrEqualTo(N):
    return len(fibsLessThanOrEqualTo(N))  # Just return the length of the list

# Function to display the available commands to the user
def displayHelpMessage():
    print("The following commands are available:")
    print("  0: Exit.")
    print("  1: List the first N Fibonacci numbers.")
    print("  2: Display the nth Fibonacci number (0-based).")
    print("  3: List the Fibonacci numbers less or equal to N.")
    print("  4: How many Fibonacci numbers are less or equal to N?")
    print("  5: Display this help message. ")

# Main function that runs the interactive Fibonacci Laboratory
def main():
    print("\nWelcome to the Fibonacci Number laboratory!")
    print()
    displayHelpMessage()  # Show commands at the start
    
    ERROR_MESSAGE = "ERROR: Illegal value entered."
    COMMAND_ERROR = "ERROR: Illegal command. Try again."
    
    while True:
        print()
        command = input("Please enter a command (0, 1, 2, 3, 4, or 5): ")
        
        # Exit command
        if command == "0" or command.lower() == "exit" or command.lower() == "quit":
            print("\nThanks for using the Fibonacci Laboratory! Goodbye.")
            break
        
        # Help message command
        elif command == "5" or command == "?" or command.lower() == "help":
            displayHelpMessage()
        
        # Command to list first N Fibonacci numbers
        elif command == "1":
            nString = input("You've asked for the first N Fibonacci numbers. What is N? ")
            if nString.isdigit():
                n = int(nString)
                if n >= 0:
                    print(firstNFibNumbers(n))  # Call and print result
                else:
                    print(ERROR_MESSAGE)
            else:
                print(ERROR_MESSAGE)
        
        # Command to get nth Fibonacci number
        elif command == "2":
            nString = input("You've asked for the nth Fibonacci number. What is n? ")
            if nString.isdigit():
                n = int(nString)
                if n >= 0:
                    print(nthFibNumber(n))  # Call and print result
                else:
                    print(ERROR_MESSAGE)
            else:
                print(ERROR_MESSAGE)
        
        # Command to list Fibonacci numbers ≤ N
        elif command == "3":
            nString = input("You've asked for the Fibonacci numbers less than or equal to N. What is N? ")
            try:
                n = int(nString)
                if n >= 0:
                    print(fibsLessThanOrEqualTo(n))  # Call and print result
                else:
                    print(ERROR_MESSAGE)
            except ValueError:
                print(ERROR_MESSAGE)
        
        # Command to count Fibonacci numbers ≤ N
        elif command == "4":
            nString = input("You've asked how many Fibonacci numbers are less than or equal to N. What is N? ")
            try:
                n = int(nString)
                if n >= 0:
                    print(countFibsLessThanOrEqualTo(n))  # Call and print result
                else:
                    print(ERROR_MESSAGE)
            except ValueError:
                print(ERROR_MESSAGE)
        
        # Catch invalid command
        else:
            print(COMMAND_ERROR)
            displayHelpMessage()

# Call main function to start the program
main()
