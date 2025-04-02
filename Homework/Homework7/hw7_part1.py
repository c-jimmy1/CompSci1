"""
This is homework 7 part 1, and will simulate an autocorrect feature given a dictionary of words.
We will be taking in 3 inputs, the dictionary, the words to be corrected, and the keyboard layout.

Author: Jimmy Chen
Version: 1
"""

def parse_dictionary(dict_file):
    """"Parses the dictionary file and returns a dict of words with their frequencies"""
    word_dict = {}
    with open(dict_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into word and frequency by comma
            word, frequency = line.strip().split(",")
            word_dict[word] = float(frequency)

    return word_dict

def parse_keyboard(keyboard_file):
    """Parses the keyboard file and returns a dict"""
    keyboard_neighbors = {}
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

def process_word(words, keyboard_nbrs, word_dict):
    """For each word, check if it is in the dictionary. If it isn't consider candidate corrections."""
    for word in words:
        candidates = []
        spaces_length = 15 - len(word)
        spaces = spaces_length * ' '
        if word in word_dict:
            print('{}{} -> FOUND'.format(spaces, word))
            


def main():
    # dict_file = input("Dictionary file => ").strip()
    # print(dict_file)
    # input_file = input("Input file => ").strip()
    # print(input_file)
    # keyboard_file = input("Keyboard file => ").strip()
    # print(keyboard_file)

    dict_file = "words_10percent.txt"
    input_file = "input_words.txt"
    keyboard_file = "keyboard.txt"

    word_dictionary = parse_dictionary(dict_file)
    keyboard_neighbors = parse_keyboard(keyboard_file)
    words = parse_input(input_file)

    process_word(words, keyboard_neighbors, word_dictionary)

if __name__ == "__main__":
    main()