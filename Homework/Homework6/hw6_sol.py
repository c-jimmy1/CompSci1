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


def get_len_words(words):
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
            word_dict[length] = set()
            print("{:4d}:{:4d}:".format(length, 0))
        else:
            if count <= 6:
                print("{:4d}:{:4d}: {:s}".format(length, count, ' '.join(length_words)))
            else:
                first_three = ' '.join(length_words[:3])
                last_three = ' '.join(length_words[-3:])
                print("{:4d}:{:4d}: {:s} ... {:s}".format(length, count, first_three, last_three))

    return word_dict
        
        
def get_word_pairs(words, max_sep):
    """
    Given a list of words and a maximum separation `max_sep`,
    return a set of (word1, word2) pairs (in alphabetical order)
    that occur within `max_sep` positions of each other in the list.
    """
    pairs = []
    n = len(words)
    
    # For each word, look up to max_sep words ahead
    for i in range(n):
        # j goes from i+1 up to i+max_sep (inclusive), but not beyond n
        for j in range(i+1, min(n, i + max_sep + 1)):
            pair = tuple(sorted((words[i], words[j])))
            pairs.append(pair)
        
    distinct_sorted_pairs = sorted(set(pairs))

    print("  {:d} distinct pairs".format(len(distinct_sorted_pairs)))
    
    if len(distinct_sorted_pairs) > 10:
        for p in distinct_sorted_pairs[:5]:
            print("  {:s} {:s}".format(p[0], p[1]))
        print("  ...")
        for p in distinct_sorted_pairs[-5:]:
            print("  {:s} {:s}".format(p[0], p[1]))
    else:
        for p in distinct_sorted_pairs:
            print("  {:s} {:s}".format(p[0], p[1]))
    
    # Print the ratio of distinct word pairs to total word pairs
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(len(distinct_sorted_pairs)/len(pairs)))
    
    return distinct_sorted_pairs


def process_document(file):
    """Read a file, clean it, remove stop words, and process it. Handles all the printing and stats for each document."""
    print("\nEvaluating document {}".format(file))
    words = parse_clean_file(file)
    words = remove_stop_words(words)
    
    avg_word_length = calc_avg_word_length(words)
    print("1. Average word length: {:.2f}".format(avg_word_length))    
    
    ratio_distinct = calc_ratio_distinct(words)
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio_distinct))
        
    print("3. Word sets for document {}:".format(file))
    lengths = get_len_words(words)
    
    print("4. Word pairs for document {}".format(file))
    pairs = get_word_pairs(words, max_sep)
    
    return words, avg_word_length, ratio_distinct, lengths, pairs

def jaccard_similarity(length_sets, length_sets2):
    """Given two dicts of sets, calculate the Jaccard similarity for each corresponding set in the dicts."""
    
    # Get the set of all lengths that appear in either dict
    all_lengths = set(length_sets.keys()).union(set(length_sets2.keys()))
    
    # Calculate Jaccard similarities for corresponding sets
    jaccard_list = []
    for length in sorted(all_lengths):
        set1 = length_sets.get(length, set())
        set2 = length_sets2.get(length, set())
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        jaccard = len(intersection) / len(union) if union else 0
        jaccard_list.append(jaccard)
    
    return jaccard_list

if __name__ == "__main__":
    file1 = input('Enter the first file to analyze and compare ==> ').strip()
    print(file1)
    
    file2 = input('Enter the second file to analyze and compare ==> ').strip()
    print(file2)
    
    max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
    print(max_sep)
    max_sep = int(max_sep)
    
    words1, avg_word_length1, ratio_distinct1, lengths1, pairs1 = process_document(file1)
    words2, avg_word_length2, ratio_distinct2, lengths2, pairs2 = process_document(file2)
    
    # Summary Comparison
    print('\nSummary comparison')
    
    if avg_word_length1 > avg_word_length2:
        print("1. {} on average uses longer words than {}".format(file1, file2))
    else:
        print("1. {} on average uses longer words than {}".format(file2, file1))
        
    overall_jaccard = len(set(words1).intersection(set(words2))) / len(set(words1).union(set(words2)))
    
    print('2. Overall word use similarity: {:.3f}'.format(overall_jaccard))

    print('3. Word use similarity by length:')
    similarities = jaccard_similarity(lengths1, lengths2)
    for i, sim in enumerate(similarities):
        print('{:4d}: {:.4f}'.format(i+1, sim))
        
    jaccard_similarity_pairs = len(set(pairs1).intersection(set(pairs2))) / len(set(pairs1).union(set(pairs2)))
    print('4. Word pair similarity: {:.4f}'.format(jaccard_similarity_pairs))