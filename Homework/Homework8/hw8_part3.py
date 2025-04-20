"""
HW 8 - Part 3 driver program.  Runs the full Bears & Berries simulation
with reserve queues and extended stopping/ reporting rules.

Author: Jimmy Chen
"""

import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist


def print_state(field: BerryField):
    """print the current state of the simulation (berries + grid + actors)."""
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

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    
    # Instantiate objects with the data from the JSON file
    active_bears = [Bear(r, c, d) for r, c, d in data.get("active_bears", [])]
    active_tourists = [Tourist(r, c) for r, c in data.get("active_tourists", [])]

    field = BerryField(data["berry_field"], active_bears, active_tourists)

    # Reserve queues will be simple lists of the raw tuples so we can lazily
    reserve_bears = list(data.get("reserve_bears", []))
    reserve_tourists = list(data.get("reserve_tourists", []))

    # Print the initial state
    print("\nStarting Configuration")
    print_state(field)

    # Run the simulation
    turn = 1
    
    # Loop until there are no active bears or tourists left in the field
    while True:
        no_active_bears = len(field.active_bears) == 0
        no_reserve_bears = len(reserve_bears) == 0
        if (no_active_bears and no_reserve_bears) or (
            no_active_bears and field.berry_total() == 0
        ):
            # Always show final state if it was *not* just printed.
            if turn == 1 or (turn - 1) % 5 != 0:
                print_state(field)
            break

        print(f"\nTurn: {turn}")

        field.grow()

        # Move and feed bears
        i = 0
        while i < len(field.active_bears):
            bear = field.active_bears[i]
            msgs, gone = bear.take_turn(field, field.active_tourists)
            for m in msgs:
                print(m)
            if gone:
                field.active_bears.pop(i)
            else:
                i += 1
                
        # While there are active tourists
        j = 0
        while j < len(field.active_tourists):
            tourist = field.active_tourists[j]
            if tourist.take_turn(field.active_bears):
                # If the tourist leaves the field, remove them from the list
                print(f"{tourist} - Left the Field")
                field.active_tourists.pop(j)
            else:
                j += 1

        # If there any reserve bears in the queue and the field has at least 500 berries, add one to the field
        if reserve_bears and field.berry_total() >= 500:
            r, c, d = reserve_bears.pop(0)
            new_bear = Bear(r, c, d)
            field.active_bears.append(new_bear)
            print(f"{new_bear} - Entered the Field")

        # Check if any tourists are in the field and if there are any reserve tourists
        # If there are, add one to the field
        if reserve_tourists and field.active_bears:
            r, c = reserve_tourists.pop(0)
            new_tourist = Tourist(r, c)
            field.active_tourists.append(new_tourist)
            print(f"{new_tourist} - Entered the Field")


        if turn % 5 == 0:
            print_state(field)


        turn += 1
        print()


if __name__ == "__main__":
    main()
