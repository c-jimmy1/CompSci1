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
        print("Length: +1")
        return 1
    elif len(password) >= 8 and len(password) <= 10:
        print("Length: +2")
        return 2
    elif len(password) > 10:
        print("Length: +3")
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
        print("Cases: +2")
        return 2
    elif upper >= 1 and lower >= 1:
        print("Cases: +1")
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
        print("Digits: +2")
        return 2
    elif num >= 1:
        print("Digits: +1")
        return 1
    else:
        return 0

def check_punctuation(password):
    """If it contains at least one of !@#$ add 1 and if it contains at least one of %^&*
    then add 1 (total possible of 2)."""
    count = 0
    if "!" in password or "@" in password or "#" in password or "$" in password:
        print("!@#$: +1")
        count += 1
    if "%" in password or "^" in password or "&" in password or "*" in password:
        count += 1
        print("%^&*: +1")
    return count

def check_ny_license(password):
    """If it contains three letters (upper or lower case) followed by four digits, then
    it potentially matches a NY state license plate. In this case, subtract 2 from the score."""
    if len(password) == 7 and password[:3].isalpha() and password[3:].isdigit():
        print("License: -2")
        return -2
    return 0
    
def check_top_password(password):
    """If the lower case version of the password exactly matches a password
    found in a list of common passwords, then subtract 3 from the score."""
    top_passwords = part1_get_top()
    if password.lower() in top_passwords:
        print("Common: -3")
        return -3
    return 0

def get_total_score(password):
    total_score = 0
    # Add the score from the length of the password
    length_count = check_length(password)
    total_score += length_count

    # Add the score from checking the cases of the password
    case_count = check_case(password)
    total_score += case_count

    # Add the score from checking the numbers in the password
    num_count = check_numbers(password)
    total_score += num_count

    # Add the score from checking the punctuation in the password
    punctuation_count = check_punctuation(password)
    total_score += punctuation_count
    
    # Subtract the score if the password matches a NY state license plate
    total_score += check_ny_license(password)

    # Subtract the score if the password matches a common password
    total_score += check_top_password(password)

    print("Combined score:", total_score)
    return total_score

if __name__ == "__main__":
    password = input("Enter a password => ").strip()
    print(password)
    
    score = get_total_score(password)

    if score <= 0:
        print("Password is rejected")
    elif score == 1 or score == 2:
        print("Password is poor")
    elif score == 3 or score == 4:
        print("Password is fair")
    elif score == 5 or score == 6:
        print("Password is good")
    else:
        print("Password is excellent")

    



