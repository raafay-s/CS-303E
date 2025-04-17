# Assignment: HW9
# File: MyListFunctions.py
# Student: Mohammad Raafay Shehzad 
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date: 03/11/2025
# Description of Program: This program implements various list manipulation functions without using built-in list methods, except for allowed ones.

# Function to append an element to a list
def myAppend(lst, x):
    return lst + [x]

# Function to extend a list with another list
def myExtend(lst1, lst2):
    new_list = lst1[:]
    for item in lst2:
        new_list += [item]
    return new_list

# Function to find the maximum value in a list
def myMax(lst):
    if not lst:
        print("Empty list: no max value")
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

# Function to sum all elements in a list
def mySum(lst):
    total = 0
    for item in lst:
        total += item
    return total

# Function to count occurrences of an element in a list
def myCount(lst, x):
    count = 0
    for item in lst:
        if item == x:
            count += 1
    return count

# Function to insert an element at a specific index
def myInsert(lst, i, x):
    if i < 0 or i > len(lst):
        print("Invalid index")
        return None
    return lst[:i] + [x] + lst[i:]

# Function to remove and return an element at a given index
def myPop(lst, i):
    if i < 0 or i >= len(lst):
        print("Invalid index")
        return lst, None
    return lst[:i] + lst[i+1:], lst[i]

# Function to find the index of the first occurrence of an element
def myFind(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

# Function to find the index of the last occurrence of an element
def myRFind(lst, x):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == x:
            return i
    return -1

# Function to find all indices of an element in a list
def myFindAll(lst, x):
    indices = []
    for i in range(len(lst)):
        if lst[i] == x:
            indices += [i]
    return indices

# Function to return a reversed version of the list
def myReverse(lst):
    return lst[::-1]

# Function to remove the first occurrence of an element
def myRemove(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return lst[:i] + lst[i+1:]
    return lst

# Function to remove all occurrences of an element
def myRemoveAll(lst, x):
    return [item for item in lst if item != x]

# Function to check if two lists are equal
def myEqual(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

# Function to check if all elements in a list are equal to a given value
def allEqual(lst, x):
    for item in lst:
        if item != x:
            return False
    return True

# Function to slice a list without using slicing notation
def mySlice(lst, i, j):
    if i < 0 or j > len(lst):
        print("Illegal index value")
        return []
    new_list = []
    for index in range(i, j):
        new_list += [lst[index]]
    return new_list