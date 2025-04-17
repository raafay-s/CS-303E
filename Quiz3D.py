# CS 303E Quiz 3D
# do NOT rename this file, otherwise Gradescope will not accept your submission


# Problem 1: Pairwise Swap
def swap(values):
    # write your solution to problem 1 here
    result = []
    
    # Handle empty list case
    if not values:
        return []
    
    # Check if list has odd length (has unpaired value)
    if len(values) % 2 != 0:
        # Extract the unpaired value (last one)
        unpaired = values.pop()
        # We'll add it to the beginning later
    else:
        unpaired = None
    
    # Process pairs
    i = 0
    while i < len(values):
        # Add the second element of the pair first, then the first element
        result.append(values[i+1])
        result.append(values[i])
        i += 2
    
    # Add unpaired value at the beginning if it exists
    if unpaired is not None:
        result.insert(0, unpaired)
    
    return result
    pass

# Problem 2: Factors in Line
def factorsInLine(values):
    # write your solution to problem 2 here
    if not values:
        return []
    
    result = []
    current_sublist = []
    
    for value in values:
        # If current_sublist is empty or if the current value is not a multiple of the anchor
        # (first element in the current sublist), start a new sublist
        if not current_sublist or value % current_sublist[0] != 0:
            # If we already have a sublist, add it to the result
            if current_sublist:
                result.append(current_sublist)
            # Start a new sublist with the current value as the anchor
            current_sublist = [value]
        else:
            # Current value is a multiple of the anchor, add it to the current sublist
            current_sublist.append(value)
    
    # Don't forget to add the last sublist if it exists
    if current_sublist:
        result.append(current_sublist)
    
    return result
    pass



if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # You may, however, change these to test different components
    # print(swap([6, 3, 19, 19, 12, 6, 15]))
    # print(factorsInLine([6, 3, 19, 19, 12, 6, 15, 30]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT