def merge(L1,L2):

    i1, i2 = 0, 0
    L = []
    
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            L.append( L1[i1] )
            i1 += 1
        elif L1[i1] == L2[i2]:
            L.append(L1[i1])
            i1 += 1
            i2 += 2
        else:
            L.append( L2[i2] )
            i2 += 1
    L.extend(L1[i1:])
    L.extend(L2[i2:])
    return L 

if __name__ == "__main__":
    L1 = [ 2, 7, 9, 12, 17, 18, 22, 25 ]
    L2 = [ 1, 5, 6, 8, 13, 14, 15, 18, 19, 23, 25 ]

    merged_L = merge(L1, L2)
    print(merged_L)
