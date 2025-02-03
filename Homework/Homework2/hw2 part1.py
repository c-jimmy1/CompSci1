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
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def find_volume_cube(side):
    # This function calculates the volume of a cube given the side length.
    # The formula for the volume of a cube is: side^3
    volume = side ** 3
    return volume


if __name__ == "__main__":
    # This is the main function that will run the program.

    # Ask the user for the radius of the gumball and the weekly sales, and convert them to the correct data type.
    gumball_radius = input("Enter the gum ball radius (in.) => ").strip()
    print(gumball_radius)
    gumball_radius = float(gumball_radius)

    weekly_sales = input("Enter the weekly sales => ").strip()
    print(weekly_sales)
    weekly_sales = int(weekly_sales)

    # Calculate the target sales, the number of gumballs on the edge, the side length of the machine, and the extra gumballs.
    target_sales = math.ceil(weekly_sales * 1.25)
    gumballs_on_edge = math.ceil(target_sales ** (1/3))
    side_length = (2 * gumball_radius) * gumballs_on_edge
    extra_gumballs = (gumballs_on_edge ** 3) - target_sales

    # Calculate the volume of the cube and the volume of the sphere, and then calculate the wasted space.
    volume_cube = find_volume_cube(side_length)
    volume_ball = find_volume_sphere(gumball_radius)
    wasted_space_target = volume_cube - (target_sales * volume_ball)
    wasted_space_filled = volume_cube - (gumballs_on_edge ** 3 * volume_ball)

    # Print the results out to the user.
    print("The machine needs to hold {} gum balls along each edge.".format(gumballs_on_edge))
    print("Total edge length of the machine is {:.2f} inches.".format(side_length))
    print("Target sales were {}, but the machine will hold {} extra gum balls.".format(target_sales, extra_gumballs))
    print("Wasted space is {:.2f} cubic inches with the target number of gum balls,\nor {:.2f} if you fill up the machine.".format(wasted_space_target, wasted_space_filled))