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
    with open(file, 'r') as f:
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

    for word in word_list:
        if word in stop_words:
            word_list.remove(word)
    
    return word_list

if __name__ == "__main__":
    file1 = "ex1.txt" # input('Enter the first file to analyze and compare ==> ').strip()
    print(file1)
    
    file2 = "ex2.txt" # input('Enter the second file to analyze and compare ==> ').strip()
    print(file2)
    
    max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
    print(max_sep)
    max_sep = int(max_sep)
    
    file1_words = parse_clean_file(file1)
    file2_words = parse_clean_file(file2)
    
    file1_words = remove_stop_words(file1_words)
    file2_words = remove_stop_words(file2_words)
    
    print(file1_words)
    