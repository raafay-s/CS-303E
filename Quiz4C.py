# CS 303E Quiz 4C
# do NOT rename this file, otherwise Gradescope will not accept your submission


# Problem 1: Last Vowel Locations
def lastVowelLocations(strings):
    vowels = set("aeiouAEIOU")
    result = {}
    for word in strings:
        last_index = -1
        for i in range(len(word)):
            if word[i] in vowels:
                last_index = i
        result[word] = last_index
    return result

# Problem 2: Zerosum Triplets
def zerosumTriplets(values):
    result = set()
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if values[i] + values[j] + values[k] == 0:
                    triplet = tuple(sorted([values[i], values[j], values[k]]))
                    result.add(triplet)
    return result


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # You may, however, change these to test different components
    # print(lastVowelLocations({'apple', 'pteradactyl', 'bcdfghjklmnpqrstvwxyz'}))
    # print(zerosumTriplets([-1, 1, 0, 2]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT