points = [ (4,2), (1,-3), (-4, -6), (6,9), (3,8), (-5,2), (6,2) ]
min_x = min(map(lambda p: p[0], filter(lambda p: p[0] > 0 and p[1] > 0, points)))
print(min_x)
