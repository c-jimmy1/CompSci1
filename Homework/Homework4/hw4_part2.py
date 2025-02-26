""" This program uses a 2019 corona virus dataset and analyzes the data to conclude on some statistics.
We will compare stats about each state, and many more.
Author: Jimmy Chen
Version: 1
"""

import hw4_util

def input_loop():
    week_number = 0

    while week_number >= 0:
        week_number = input("Please enter the index for a week: ").strip()
        print(week_number)
        week_number = int(week_number)

        week_data = hw4_util.part2_get_week(week_number)
        if not week_data:
            continue

        user_request = input("Request (daily, pct, quar, high): ").strip()
        print(user_request)

        if user_request == "daily":
            pass
        elif user_request == "pct":
            pass
        elif user_request == "quar":
            pass
        elif user_request == "high":
            pass
            


        
if __name__ == "__main__":
    input_loop()