import math

radius_1 = 5
area = math.pi * (radius_1 ** 2)
formatted_area = "{:.2f}".format(area)
print("Area 1 =", formatted_area)

radius_2 = 32
area = math.pi * pow(radius_2, 2)
formatted_area = round(area, 2)
print("Area 2 =", formatted_area)