"""This program take in an input of a password and determines 
if the password is strong or weak. 
Author: Jimmy Chen
Version: 1
"""

from hw4_util import part1_get_top


def check_length(password):
    """Check the length of the password. If the password is 6 or 7 characters long,
    then return 1. If the password is 8, 9, or 10 characters long, then return 2. If the
    password is longer than 10, add 3 to the score. Otherwise, return 0."""

    if len(password) == 6 or len(password) == 7:
        return 1
    elif len(password) >= 8 and len(password) <= 10:
        return 2
    elif len(password) > 10:
        return 3
    else:
        return 0
    
def check_case(password):
    """If the password contains at least two upper case letters and two lower case letters 
    add 2 to the score, while if it contains at least one of each, add 1 to the score."""
    upper = 0
    lower = 0
    # Count the number of upper and lower case letters in the password
    for char in password:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    # Check if the password contains at least two upper case letters and two lower case letters
    if upper >= 2 and lower >= 2:
        return 2
    elif upper >= 1 and lower >= 1:
        return 1
    else:
        return 0
    

def check_numbers(password):
    """If it contains at least two digits add 2 to the score and if it contains at least one digit
    then add 1."""
    
    num = 0
    # Count the number of digits in the password
    for char in password:
        if char.isdigit():
            num += 1

    # Check if the password contains at least two digits
    if num >= 2:
        return 2
    elif num >= 1:
        return 1
    else:
        return 0

def check_punctuation():
    """If it contains at least one of !@#$ add 1 and if it contains at least one of %^&*
    then add 1 (total possible of 2)."""

if __name__ == "__main__":
    password = input("Enter a password => ").strip()
    print(password)
    
    total_score = 0
    # Add the score from the length of the password
    total_score += check_length(password)
    # Add the score from checking the cases of the password
    total_score += check_case(password)
    # Add the score from checking the numbers in the password
    total_score += check_numbers(password)





