def find_min(L):
    if len(L) == 0:
        return None
    min_val = L[0][0]
    for lst in L:
        for val in lst:
            if val < min_val:
                min_val = val
    return min_val

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )