# File: RecursiveFunctions.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
#
# Date: 04/08/2025
# Description of Program: Practice writing recursive functions that operate on integers, strings, and lists.

def sumItemsInList(L):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList(L[1:])

def countOccurrencesInList(key, L):
    """ Return the number of times key occurs in list L. """
    if not L:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList(key, L[1:])
    else:
        return countOccurrencesInList(key, L[1:])

def addToN(n):
    """ Return the sum of the non-negative integers to n. """
    if n == 0:
        return 0
    else:
        return n + addToN(n - 1)

def findSumOfDigits(n):
    """ Return the sum of the digits in a non-negative integer. """
    if n == 0:
        return 0
    else:
        return (n % 10) + findSumOfDigits(n // 10)

def integerToBinary(n):
    """ Given a nonnegative integer n, return the binary representation as a string. """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return integerToBinary(n // 2) + str(n % 2)

def integerToList(n):
    """ Given a nonnegative integer, return a list of the digits (as strings). """
    if n < 10:
        return [str(n)]
    else:
        return integerToList(n // 10) + [str(n % 10)]

def isPalindrome(s):
    """ Return True if string s is a palindrome and False otherwise. """
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])

def findFirstUppercase(s):
    """ Return the first uppercase letter in string s, if any. """
    if not s:
        return None
    elif s[0].isupper():
        return s[0]
    else:
        return findFirstUppercase(s[1:])

def findLastUppercase(s):
    """ Return the last uppercase letter in string s, if any. """
    if not s:
        return None
    result = findLastUppercase(s[:-1])
    if s[-1].isupper():
        return s[-1]
    else:
        return result

def negateItems(lst):
    """ Assume lst is a list of numbers. Return a list of the negations of those numbers. """
    if not lst:
        return []
    else:
        return [-lst[0]] + negateItems(lst[1:])

def findFirstUppercaseIndexHelper(s, index):
    """ Return the offset of the first uppercase letter; assume you are starting at index. """
    if not s:
        return -1
    elif s[0].isupper():
        return index
    else:
        return findFirstUppercaseIndexHelper(s[1:], index + 1)
    
def findFirstUppercaseIndex(s):
    """ Return the index of the first uppercase letter in string s, if any. """
    return findFirstUppercaseIndexHelper(s, 0)