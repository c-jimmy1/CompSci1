"""
This is homework 7 part 1, and will simulate an autocorrect feature given a dictionary of words.
We will be taking in 3 inputs, the dictionary, the words to be corrected, and the keyboard layout.

Author: Jimmy Chen
Version: 1
"""

def parse_dictionary(dict_file):
    """"Parses the dictionary file and returns a dict of words with their frequencies"""
    word_dict = dict()
    with open(dict_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into word and frequency by comma
            word, frequency = line.strip().split(",")
            word_dict[word] = float(frequency)

    return word_dict

def parse_keyboard(keyboard_file):
    """Parses the keyboard file and returns a dict"""
    keyboard_neighbors = dict()
    with open(keyboard_file, 'r', encoding='utf-8') as file:
        for line in file:
            letters = line.strip().split()
            if letters:
                # The first letter is the key, and the rest are its neighbors
                key = letters[0]
                neighbors = letters[1:]
                keyboard_neighbors[key] = neighbors

    return keyboard_neighbors

def parse_input(input_file):
    """Parses the input file and returns a list of words"""
    with open(input_file, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

def drop(word, word_dict):
    """Drop a letter from the word and check if it is in the dictionary"""
    candidates = []
    for i in range(len(word)):
        # Create a candidate word by dropping the letter at position i
        candidate = word[:i] + word[i+1:]
        if candidate in word_dict:
            candidates.append(candidate)
    return candidates

def swap(word, word_dict):
    """Swap two adjacent letters in the word and check if it is in the dictionary"""
    candidates = []
    for i in range(len(word) - 1):
        # Swap the letters at position i and i+1
        candidate = word[:i] + word[i+1] + word[i] + word[i+2:]
        if candidate in word_dict:
            candidates.append(candidate)
    return candidates
    
def replace(word, word_dict, keyboard_nbrs):
    """Replace a letter with its keyboard neighbors and check if it is in the dictionary"""
    candidates = []
    for i in range(len(word)):
        letter = word[i]
        # Check if the letter is in the keyboard neighbors
        if letter in keyboard_nbrs:
            for neighbor in keyboard_nbrs[letter]:
                # Create a candidate word by replacing the letter with its neighbor
                candidate = word[:i] + neighbor + word[i+1:]
                if candidate in word_dict:
                    candidates.append(candidate)
    return candidates

def insert(word, word_dict, keyboard_nbrs):
    """Insert a letter from the keyboard neighbors and check if it is in the dictionary"""
    candidates = []
    for i in range(len(word) + 1):
        for letter in keyboard_nbrs:
            # Create a candidate word by inserting the letter at position i
            candidate = word[:i] + letter + word[i:]
            if candidate in word_dict:
                candidates.append(candidate)
    return candidates

def sort_words_by_freq(word_dict, potential):
    """Removing duplicates and sorting by greatest freq to least"""

    set_potential = set(potential)
    valid_words = set_potential.intersection(word_dict.keys())
    sorted_words = sorted(valid_words, key=lambda w: word_dict[w], reverse=True)
    
    return sorted_words

def process_word(words, keyboard_nbrs, word_dict):
    """For each word, check if it is in the dictionary. If it isn't consider candidate corrections."""
    for word in words:
        candidates = []
        spaces_length = 15 - len(word)
        spaces = spaces_length * ' '
        if word in word_dict:
            print('{}{} -> FOUND'.format(spaces, word))
        else:
            candidates.extend(drop(word, word_dict))
            candidates.extend(swap(word, word_dict))
            candidates.extend(replace(word, word_dict, keyboard_nbrs))
            candidates.extend(insert(word, word_dict, keyboard_nbrs))
            
            candidates = list(set(candidates))
            candidates = sort_words_by_freq(word_dict, candidates)
            num_found = len(candidates)

            # Print the results based on the number of candidates found
            if num_found == 0:
                print('{}{} -> NOT FOUND'.format(spaces, word))
            elif num_found == 1:
                print('{}{} -> FOUND{:3d}:  {}'.format(spaces, word, num_found, candidates[0]))
            elif num_found == 2:
                print('{}{} -> FOUND{:3d}:  {} {}'.format(spaces, word, num_found, candidates[0], candidates[1]))
            else:
                print('{}{} -> FOUND{:3d}:  {} {} {}'.format(
                    spaces, word, num_found, candidates[0], candidates[1], candidates[2]))


def main():
    # Prompt the user for the dictionary, input, and keyboard files
    dict_file = input("Dictionary file => ").strip()
    print(dict_file)
    input_file = input("Input file => ").strip()
    print(input_file)
    keyboard_file = input("Keyboard file => ").strip()
    print(keyboard_file)

    # Parse the files
    word_dictionary = parse_dictionary(dict_file)
    keyboard_neighbors = parse_keyboard(keyboard_file)
    words = parse_input(input_file)

    # Process each word in the input file
    process_word(words, keyboard_neighbors, word_dictionary)

if __name__ == "__main__":
    main()