"""
This is homework 8 part 1. This part of the homework has to do with reading a json and parsing
each data into the respective classes.

Author: Jimmy Chen
Version: 1
"""
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist
import json


def main():
    json_file = input("Enter the json file name for the simulation => ").strip()
    print(json_file)  # echo back exactly like the sample output

    with open(json_file) as f:
        data = json.load(f)

    # Instantiate objects ------------------------------------------------
    active_bears    = [Bear(r, c, d) for r, c, d in data["active_bears"]]
    active_tourists = [Tourist(r, c)  for r, c   in data["active_tourists"]]

    field = BerryField(data["berry_field"], active_bears, active_tourists)

    # Print the initial state --------------------------------------------
    print(f"\nField has {field.berry_total()} berries.")
    print(field, end="\n\n")

    print("Active Bears:")
    for b in active_bears:
        print(b)
    print("\nActive Tourists:")
    for t in active_tourists:
        print(t)


if __name__ == "__main__":
    main()