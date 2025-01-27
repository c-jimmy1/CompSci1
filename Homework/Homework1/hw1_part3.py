import math

character = input("Enter frame character  ==> ").strip()
print(character)

height = (input("Height of box ==> ")).strip()
print(height)

width = (input("Width of box ==> ")).strip()
print(width)

total_char = len(width) + len(height) + 1

height = int(height)
width = int(width)

total_space = width - 2 - total_char
left_space = math.floor((total_space/2))
right_space = total_space - left_space

totalVertical = height - 3
up_space = math.floor((totalVertical/2))
down_space = totalVertical - up_space

print("\nBox:")
print(character * width)
print((character + " " * (width - 2) + character + "\n") * (up_space - 1) + (character + " " * (width - 2) + character))
print(character + " " * left_space + str(width) + "x" + str(height) + " " * right_space + character)
print((character + " " * (width - 2) + character + "\n") * (down_space - 1) + (character + " " * (width - 2) + character))
print(character * width)
 
