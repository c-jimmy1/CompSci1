def first_day_greater(L1, L2):
    """
    L1 and L2 are lists of numbers. 
    Returns the first day on which the value in L1 is greater than the corresponding value in L2.
    If there is no such day, returns -1.
    """
    for i in range(len(L1)):
        if L1[i] > L2[i]:
            return i
    return -1


if __name__ == "__main__":
    L1 = [ 15.1, 17.3, 12.3, 16.4 ]
    L2 = [ 15.0, 17.7, 12.5, 16.9 ]
    print("Test 1: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.6, 17.9, 18.2, 16.5, 12.7 ]
    print("Test 2: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.9, 18.8, 11.4 ]
    print("Test 3: {}".format( first_day_greater(L1,L2) ))