# Assignment: HW8
# File: MyStringFunctions.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date: 03/10/2025
# Description of Program: Implementing a string library with functions that mimic built-in string operations.

# Append a character to the end of a string
def myAppend(s, ch):
    return s + ch

# Count occurrences of a character in a string
def myCount(s, ch):
    count = 0
    for char in s:
        if char == ch:
            count += 1
    return count

# Concatenate two strings
def myExtend(s1, s2):
    return s1 + s2

# Find the smallest character in a string
def myMin(s):
    if not s:
        print("Empty string: no min value")
        return None
    min_char = s[0]
    for char in s:
        if char < min_char:
            min_char = char
    return min_char

# Insert a character at a specified index
def myInsert(s, i, ch):
    if i < 0 or i > len(s):
        print("Invalid index")
        return None
    return s[:i] + ch + s[i:]

# Remove and return a character at a specified index
def myPop(s, i):
    if i < 0 or i >= len(s):
        print("Invalid index")
        return s, None
    return s[:i] + s[i+1:], s[i]

# Find the first occurrence of a character
def myFind(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1

# Find the last occurrence of a character
def myRFind(s, ch):
    for i in range(len(s)-1, -1, -1):
        if s[i] == ch:
            return i
    return -1

# Remove the first occurrence of a character
def myRemove(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return s[:i] + s[i+1:]
    return s

# Remove all occurrences of a character
def myRemoveAll(s, ch):
    result = ""
    for char in s:
        if char != ch:
            result += char
    return result

# Check if two strings are equal
def myEqual(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

# Check if a string contains only digits
def myIsdigit(s):
    if not s:
        return False
    for char in s:
        if char < '0' or char > '9':
            return False
    return True

# Reverse a string without using slicing
def myReverse(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

# Check if a string is a palindrome
def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    return True