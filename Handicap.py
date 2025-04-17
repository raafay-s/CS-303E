# File: Handicap.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date: 01/31/2025
# Description of Program: This program calculates the average bowling score and handicap for a player based on their scores in three games.


# Player input:
name = input("\nEnter bowler name: ")
game_one = int(input("Enter Game 1: "))
game_two = int(input("Enter Game 2: "))
game_three = int(input("Enter Game 3: "))

# Calculations for average and handicap:
average = int((game_one + game_two + game_three) / 3)
handicap = int((200 - average) * 0.8)
handicap = max( 0, handicap )

# Player summary:
print("\nHandicap Report for " + name + ":")
print("  " + name + "'s average is: " + str(average))
print("  " + name + "'s handicap is: " + str(handicap))
print("\nIt's time to Bowl!\n")
