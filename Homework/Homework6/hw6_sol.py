"""
This is homework 6, which covers nlp processing. We will be taking in two text files containing two different
documents and will be comparing the two documents. We will be comparing the two documents using the Jaccard
similarity metric. 

Author: Jimmy Chen
Version: 1
"""

def parse_clean_file(file):
    """
    Reads a file and returns a list of words with non-letter characters removed
    and all letters converted to lowercase.
    """
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    cleaned_words = []

    # Remove non-letter characters and convert to lowercase
    for word in words:
        cleaned = []
        
        # add each letter to cleaned list
        for char in word:
            if char.isalpha():
                cleaned.append(char.lower())

        # if there are letters in the word, add it to the cleaned_words list
        if len(cleaned) > 0:
            cleaned_word = ""
            for c in cleaned:
                cleaned_word += c
            cleaned_words.append(cleaned_word)

    return cleaned_words


def remove_stop_words(word_list):
    """If a word is in the stop_words set, remove it from the list."""
    stop_words = set(parse_clean_file("stop.txt"))

    new_word_list = []
    for word in word_list:
        if word not in stop_words:
            new_word_list.append(word)
    return new_word_list


def calc_avg_word_length(words):
    """Calculate the avg word length of the words in the list."""
    total_length = 0
    for word in words:
        total_length += len(word)

    avg_length = float(total_length) / len(words)
    return avg_length


def calc_ratio_distinct(words):
    """Calculate the ratio of distinct words to total words."""
    distinct_words = set(words)
    return len(distinct_words) / len(words)

def len_words(words):
    """For each word length starting from 1, find the set of words with that length.
    Print the length and num of different words with that length, and at most 6 of these words
    If there are 6 or fewer, print them all. But if there are more than 6, print first 3 and last 3, alphabetically.
    """

    word_dict = {}
    # Create a dictionary with word lengths as keys and sets of words as values
    for w in words:
        word_len = len(w)
        if word_len not in word_dict:
            word_dict[word_len] = set()
        word_dict[word_len].add(w)

    # Figure out the maximum length to iterate up to
    max_len = max(len(w) for w in words) if words else 0

    # Loop through all lengths from 1 to max_len
    for length in range(1, max_len + 1):
        # Get the set of words with the current length
        length_words = sorted(word_dict[length]) if length in word_dict else []
        count = len(length_words)
        
        # Print the length, count, and words according to the requirements
        if length not in word_dict:
            print("{:4d}:{:4d}:".format(length, 0))
        else:
            if count <= 6:
                print("{:4d}:{:4d}: {:s}".format(length, count, ' '.join(length_words)))
            else:
                first_three = ' '.join(length_words[:3])
                last_three = ' '.join(length_words[-3:])
                print("{:4d}:{:4d}: {:s} ... {:s}".format(length, count, first_three, last_three))
        
def process_document(file):
    """Read a file, clean it, remove stop words, and process it."""
    print("Evaluating document {}".format(file))
    words = parse_clean_file(file)
    words = remove_stop_words(words)
    
    avg_word_length = calc_avg_word_length(words)
    print("1. Average word length: {:.2f}".format(avg_word_length))    
    
    ratio_distinct = calc_ratio_distinct(words)
    print("2. Ratio of distinct words to total words: {:.2f}".format(ratio_distinct))
        
    print("3. Word sets for document {}".format(file))
    len_words(words)
    

if __name__ == "__main__":
    file1 = "cat_in_the_hat.txt" # input('Enter the first file to analyze and compare ==> ').strip()
    print(file1)
    
    file2 = "pulse_morning.txt" # input('Enter the second file to analyze and compare ==> ').strip()
    print(file2)
    
    max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
    print(max_sep)
    max_sep = int(max_sep)
    
    process_document(file1)
    print()
    process_document(file2)
    
    
    