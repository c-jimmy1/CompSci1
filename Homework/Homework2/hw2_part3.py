"""
This program finds out the tone of a sentence. The user will give the program a sentence,
and depending on the keywords that the user writes, we will determine the tone, and print it out.
We will also print out the number of happiness words as +, and the number of sadness words as -.
If the sentence is neutral, we will print notify the user.

Author: Jimmy Chen
Version: 1
"""

def number_happy(sentence):
    # This function counts the number of happy words in the sentence.
    # We use .lower() to make sure that the function is case insensitive.
    sentence = sentence.lower()
    total = 0
    total += sentence.count("laugh")
    total += sentence.count("happiness")
    total += sentence.count("love")
    total += sentence.count("excellent")
    total += sentence.count("good")
    total += sentence.count("smile")
    return total

def number_sad(sentence):
    # This function counts the number of sad words in the sentence.
    # We use .lower() to make sure that the function is case insensitive.
    sentence = sentence.lower()
    total = 0
    total += sentence.count("bad")
    total += sentence.count("sad")
    total += sentence.count("terrible")
    total += sentence.count("horrible")
    total += sentence.count("problem")
    total += sentence.count("hate")
    return total

if __name__ == "__main__":
    # Ask the user for the sentence and print it out for submitty.
    sentence = input("Enter a sentence => ").strip()
    print(sentence)

    # Count the number of happy and sad words in the sentence, and print out the sentiment.
    happy_count = number_happy(sentence)
    sad_count = number_sad(sentence)
    print("Sentiment: " + happy_count * "+" +  sad_count * "-")


    # Determine the tone of the sentence and print it out.
    if happy_count > sad_count:
        print("This is a happy sentence.")
    elif sad_count > happy_count:
        print("This is a sad sentence.")
    else:
        print("This is a neutral sentence.")
