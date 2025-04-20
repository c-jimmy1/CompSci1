"""
HW 8 - Part 2 driver program. This program runs a simulation of bears and tourists in a berry field.
The simulation is based on a JSON file that contains the initial state of the field, including the positions of bears and tourists.

Author: Jimmy Chen
"""

import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist


def print_state(field):
    """Print the current state of the field, including berry count and active bears/tourists."""
    print(f"Field has {field.berry_total()} berries.")
    print(field)
    print()

    print("Active Bears:")
    for b in field.active_bears:
        print(b)
        
    print("\nActive Tourists:")
    for t in field.active_tourists:
        print(t)
    print()

def main():
    json_file = input("Enter the json file name for the simulation => ").strip()
    print(json_file)

    with open(json_file, "r") as f:
        data = json.load(f)

    bears    = [Bear(r, c, d) for r, c, d in data["active_bears"]]
    tourists = [Tourist(r, c)  for r, c    in data["active_tourists"]]
    field    = BerryField(data["berry_field"], bears, tourists)

    # print the initial state
    print("\nStarting Configuration")
    print_state(field)

    # run the turns
    for turn in range(1, 6):
        print(f"Turn: {turn}")

        # 1) grow berries
        field.grow()

        # 2) move (and feed) bears
        i = 0
        while i < len(field.active_bears):
            b = field.active_bears[i]
            msgs, gone = b.take_turn(field, field.active_tourists)
            for m in msgs:
                print(m)
            if gone:
                field.active_bears.pop(i)
            else:
                i += 1

        # 3) evaluate tourists
        j = 0
        while j < len(field.active_tourists):
            t = field.active_tourists[j]
            if t.take_turn(field.active_bears):
                print(f"{t} - Left the Field")
                field.active_tourists.pop(j)
            else:
                j += 1

        # 4) end‑of‑turn report
        print_state(field)

if __name__ == "__main__":
    main()
