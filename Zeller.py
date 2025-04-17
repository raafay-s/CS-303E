# File: Zeller.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
#
# Date:02/03/2024
# Description of Program: This program calculates the day of the week for a given date using Zeller's Congruence formula while validating user input.

def main():
    # Get the year input from the user
    Y = int(input("\nEnter year (e.g., 2008): "))
    if Y < 1753:
        # Ensure the year is valid (Gregorian calendar starts in 1753)
        print("Year must be > 1752. Illegal year entered:", Y)
        print()
        return
    
    # Get the month input from the user
    M = int(input("Enter month (1-12): "))
    if M < 1 or M > 12:
        # Ensure the month is within a valid range
        print("Month must be [1..12]. Illegal month entered:", M)
        print()
        return
    
    # Get the day input from the user
    D = int(input("Enter day of the month (1-31): "))
    if D < 1 or D > 31:
        # Ensure the day is within a valid range
        print("Day must be [1..31]. Illegal day entered:", D)
        print()
        return
    
    # Adjust month and year for Zeller's Congruence formula
    if M == 1 or M == 2:
        M += 12
        Y -= 1
    
    # Extract century (J) and year within the century (K)
    K = Y % 100
    J = Y // 100
    
    # Zeller's Congruence formula to calculate the day of the week
    H = (D + (13 * (M + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    
    # Determine the day of the week based on the value of H
    weekday = ""
    if H == 0:
        weekday = "Saturday"
    elif H == 1:
        weekday = "Sunday"
    elif H == 2:
        weekday = "Monday"
    elif H == 3:
        weekday = "Tuesday"
    elif H == 4:
        weekday = "Wednesday"
    elif H == 5:
        weekday = "Thursday"
    elif H == 6:
        weekday = "Friday"
    
    # Output the result
    print("Day of the week is", weekday)
    print()
    return

# Run the main function
main()