""" This program uses a 2019 corona virus dataset and analyzes the data to conclude on some statistics.
We will compare stats about each state, and many more.
Author: Jimmy Chen
Version: 1
"""

import hw4_util

def get_daily_pos(state_abbv, week_data):
    """This function takes in a state abbreviation and a week of data 
    and returns the average daily positives per 100K population for that state."""

    for state in week_data:
        if state[0] == state_abbv:
            # If the state abbreviation matches the input

            # Get all the covid positive days for the state
            positive_days = state[2:9]

            # Calculate the average daily positives per 100K population
            avg_daily_positives = sum(positive_days) / len(positive_days)
            total_population = state[1]
            avg_daily_per_100k = (avg_daily_positives / total_population) * 100000
            return avg_daily_per_100k

def get_pct_pos(state_abbv, week_data):
    """output the average daily percentage of tests that are positive over the week, 
    accurate to the nearest tenth of a percent."""

    for state in week_data:
        if state[0] == state_abbv:
            # If the state abbreviation matches the input

            # Get all the covid positive/negative days for the state
            positive_days = state[2:9]
            negative_days = state[9:16]

            # Calculate the average daily percentage of tests that are positive
            avg_daily_positives = (sum(positive_days) / (sum(positive_days) + sum(negative_days))) * 100
            return avg_daily_positives
            
def get_quarantine(week_data):
    """Output the list of state abbreviations, alphabetically by two-letter abbreviation,
    of travel quaratine states for the given week.
    Called quarantine state if:
    a daily average of more than 10 people per 100,000 residents tested positive in the previous seven days, or
    a daily average of more than 10% of tests were positive in the previous seven days."""

    # Initialize the list of quarantine states
    quarantine_states = []

    # Iterate through all the states
    for state in week_data:
        state_abbv = state[0]
        daily_pos = get_daily_pos(state_abbv, week_data)
        daily_pos_pct = get_pct_pos(state_abbv, week_data)

        # Check if the state is a quarantine state
        if daily_pos > 10 or daily_pos_pct > 10:
            quarantine_states.append(state_abbv)

    # Sort the list of quarantine states alphabetically by two-letter abbreviation
    quarantine_states.sort()
    return quarantine_states

def get_highest(week_data):
    """Output the two-letter abbreviation of the state that had the highest daily average
    number of positive cases per 100,000 people over the given week, and output this average
    number, accurate to the nearest tenth"""
    
    # Initialize the highest daily average number of positive cases per 100,000 people
    highest_daily_avg = 0
    highest_state_abbv = ""

    # Iterate through all the states
    for state in week_data:
        state_abbv = state[0]
        daily_pos = get_daily_pos(state_abbv, week_data)

        # Update the highest daily average number of positive cases per 100,000 people
        if daily_pos > highest_daily_avg:
            highest_daily_avg = daily_pos
            highest_state_abbv = state_abbv

    return highest_state_abbv, highest_daily_avg


def input_loop():
    """This function will prompt the user for a week number and a request type.
    It will then call the appropriate function to handle the request."""

    week_number = 0

    # While the week number is not less than 0, keep requesting new week numbers from the user and processing the data
    while week_number >= 0:
        week_number = input("...\nPlease enter the index for a week: ").strip()
        print(week_number)
        week_number = int(week_number)

        # Get the week data from the util function
        week_data = hw4_util.part2_get_week(week_number)
        if not week_data:
            continue

        # Get the user request for the type of data they want to see
        user_request = input("Request (daily, pct, quar, high): ").strip()
        print(user_request)

        # Process the user request accordingly
        if user_request.lower() == "daily":
            state_abbv = input("Enter the state: ").strip()
            print(state_abbv)
            daily_pos = get_daily_pos(state_abbv.upper(), week_data)
            print("Average daily positives per 100K population: {:.1f}".format(daily_pos))

        elif user_request.lower() == "pct":
            state_abbv = input("Enter the state: ").strip()
            print(state_abbv)
            daily_pos_pct = get_pct_pos(state_abbv.upper(), week_data)
            print("Average daily positive percent: {:.1f}".format(daily_pos_pct))

        elif user_request.lower() == "quar":
            quar_states = get_quarantine(week_data)
            print("Quarantine states:")
            hw4_util.print_abbreviations(quar_states)

        elif user_request.lower() == "high":
            get_highest(week_data)
            highest_state_abbv, highest_daily_avg = get_highest(week_data)
            print("State with highest infection rate is {}".format(highest_state_abbv))
            print("Rate is {:.1f} per 100,000 people".format(highest_daily_avg))
            
if __name__ == "__main__":
    input_loop()