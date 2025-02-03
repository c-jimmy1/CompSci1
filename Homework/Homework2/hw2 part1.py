"""
This program is helping us conduct an experiment in selling gum balls.
We want to size the machine so that it is completely full at the start
of week, so that I won't run out of gumballs before i go back to check,
and I wont have excess gumballs that I have to throw away.

Author: Jimmy Chen
Version: 1
"""
import math

def find_volume_sphere(radius):
    # This function calculates the volume of a sphere given the radius.
    # The formula for the volume of a sphere is: 4/3 * pi * r^3
    volume = 4/3 * math.pi * radius ** 3
    return volume

def find_volume_cube(side):
    # This function calculates the volume of a cube given the side length.
    # The formula for the volume of a cube is: side^3
    volume = side ** 3
    return volume


if __name__ == "__main__":
    gumball_radius = input("Enter the gum ball radius (in.) => ").strip()
    print(gumball_radius)
    gumball_radius = float(gumball_radius)