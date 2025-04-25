# Assignment: Project3
# File: Project3.py
# Student: Mohammad Raafay Shehzad
# UT EID: mrs6578
# Course Name: CS303E
# 
# Date Created: 04/20/2025
# Description of Program: This program solves scrambled Jumble words by matching them to real English words using hashing. It reports the solution, time taken, and number of comparisons, and keeps running until the user exits.
    
# Import necessary libraries
import time
import os

# List of first 30 prime numbers used for the hash function
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def hash_function(s, mod=10007):
    """
    Create a hash value for a string that's invariant to letter order.
    For each letter, multiply by its corresponding prime number.
    
    Args:
        s (str): The string to hash
        mod (int): Modulus to keep the hash value manageable
        
    Returns:
        int: Hash value between 0 and mod-1
    """
    s = s.lower()  # Convert to lowercase for consistent handling
    product = 1    # Start with multiplicative identity
    for ch in s:
        if 'a' <= ch <= 'z':  # Only process lowercase letters
            idx = ord(ch) - ord('a')  # Convert letter to 0-25 index
            product *= PRIMES[idx]    # Multiply by corresponding prime
    
    # Take modulus to keep hash value in reasonable range
    return product % mod

def createDicts(filename):
    """
    Create dictionaries of 5 and 6 letter words from a wordlist file.
    
    Args:
        filename (str): Path to wordlist file
        
    Returns:
        tuple: (dict5, dict6) dictionaries mapping hash values to lists of words
    """
    dict5 = {}  # Dictionary for 5-letter words
    dict6 = {}  # Dictionary for 6-letter words
    total_words = 0  # Counter for all words in the file
    words5 = 0  # Counter for 5-letter words
    words6 = 0  # Counter for 6-letter words
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().lower()  # Remove whitespace and lowercase
                total_words += 1  # Increment total word counter
                
                # Process 5-letter words
                if len(word) == 5:  
                    h = hash_function(word)
                    if h not in dict5:
                        dict5[h] = []
                    dict5[h].append(word)
                    words5 += 1
                
                # Process 6-letter words
                elif len(word) == 6:  
                    h = hash_function(word)
                    if h not in dict6:
                        dict6[h] = []
                    dict6[h].append(word)
                    words6 += 1
                    
    except FileNotFoundError:
        print("File does not exist.")
        exit()
    
    # Print summary statistics with careful spacing for alignment
    print("\nCreating dictionaries from file:", filename, "\n")
    print("Total words found:        " + str(total_words))
    print("  Words of length 5:        " + str(words5))
    print("  Dictionary(5) buckets:    " + str(len(dict5)))
    print("  Words of length 6:       " + str(words6))
    print("  Dictionary(6) buckets:    " + str(len(dict6)))
    
    # Return both dictionaries
    return dict5, dict6

def solve_jumble(word, dict5, dict6):
    """
    Solve a jumbled word by finding its unscrambled form.
    
    Args:
        word (str): The jumbled word to solve
        dict5 (dict): Dictionary of 5-letter words
        dict6 (dict): Dictionary of 6-letter words
    """
    word = word.lower().strip()  # Normalize input
    
    # Input validation - check for non-alphabetic characters
    if not word.isalpha():
        print("Word contains illegal characters. Try again")
        return
    
    # Input validation - check word length
    if len(word) not in [5, 6]:
        print("Word must be 5 or 6 characters long. Try again")
        return
    
    start = time.perf_counter()  # Start timing
    comparisons = 0  # Initialize comparison counter
    h = hash_function(word)  # Calculate hash value for input word
    
    # Select appropriate dictionary based on word length
    if len(word) == 5:
        bucket = dict5.get(h, [])
    else:
        bucket = dict6.get(h, [])
    
    matches = []  # List to store potential matches
    for candidate in bucket:
        comparisons += 1  # Increment comparison counter
        
        # Check if candidate has the same letters as the jumbled word
        if sorted(candidate) == sorted(word):
            matches.append(candidate)  # Add to matches
    
    # Output results
    if matches:
        print("Found word:", matches[0])
    else:
        print("Sorry.  I can't solve this jumble!  Try again.")
    
    end = time.perf_counter()  # Stop timing
    print("Solving this jumble took %2.5f seconds" % (end - start))
    print("Made  ", comparisons, " comparisons.")

def main():
    """
    Main program to handle user interaction and program flow.
    """
    # Get filename from user and verify existence
    filename = input("Enter wordlist filename: ").strip()
    if not os.path.isfile(filename):
        print("File does not exist.")
        return
    
    # Create dictionaries from wordlist file
    dict5, dict6 = createDicts(filename)
    
    # Main interaction loop
    while True:
        user_input = input("\nEnter a scrambled word (or EXIT): ").strip()
        if user_input.lower() == 'exit':  # Check for exit condition
            print("Thanks for playing!  Goodbye.")
            break
        solve_jumble(user_input, dict5, dict6)  # Solve the jumble

# Run main function
main()