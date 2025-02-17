"""
This program computes a type of population balance balance problem, with bearrs, berry fields, and tourists.

Author: Jimmy Chen
Version: 1
"""

import math


def calculate_tourists(bears):
    """
    Calculate the number of tourists based on the number of bears.
      - If bears < 4 or bears > 15, tourists = 0.
      - If bears is between 4 and 10 (inclusive), each bear brings 10,000 tourists.
      - If bears is over 10, the first 10 bears bring 100,000 tourists total,
        and each additional bear brings 20,000 tourists.
    """
    tourist_count = 0
    if bears < 4 or bears > 15:
        tourist_count = 0
    elif bears <= 10:
        tourist_count = bears * 10000
    else:
        tourist_count = ((bears - 10) * 20000) + 100000

    return tourist_count


def find_next(bears, berries, tourists):
    """
    Compute the next year's number of bears and berries.
    If berries_next is negative, it is set to zero.
    """
    bears_next = berries / (50 * (bears + 1)) + bears * 0.60 - (math.log(1 + tourists, 10) * 0.1)
    berries_next = (berries * 1.5) - ((bears + 1) * (berries / 14)) - (math.log(1 + tourists, 10) * 0.05)

    berries_next = max(berries_next, 0)  # Ensure berries do not fall below 0
    return int(bears_next), berries_next


if __name__ == '__main__':
    bears = input("Number of bears => ").strip()
    print(bears)
    bears = int(bears)
    berries = input("Size of berry area => ").strip()
    print(berries)
    berries = float(berries)

    # Lists to store yearly statistics.
    bears_list = []
    berries_list = []
    tourists_list = []

    tourists = calculate_tourists(bears)

    # Print header with each column width of 10, left-aligned.
    print("{:<10}{:<10}{:<10}{:<10}".format("Year", "Bears", "Berry", "Tourists"))
    print("{:<10}{:<10d}{:<10.1f}{:<10}".format(1, bears, berries, tourists))

    # Save initial values.
    bears_list.append(bears)
    berries_list.append(berries)
    tourists_list.append(tourists)

    # Iterate for years 2 through 10.
    for year in range(2, 11):
        bears, berries = find_next(bears, berries, tourists)
        tourists = calculate_tourists(bears)

        bears_list.append(bears)
        berries_list.append(berries)
        tourists_list.append(tourists)

        print("{:<10}{:<10d}{:<10.1f}{:<10}".format(year, bears, berries, tourists))

    # Determine and print the min and max values.
    print()
    print("{:<10}{:<10d}{:<10.1f}{:<10}".format("Min:", min(bears_list), min(berries_list), min(tourists_list)))
    print("{:<10}{:<10d}{:<10.1f}{:<10}".format("Max:", max(bears_list), max(berries_list), max(tourists_list)))
