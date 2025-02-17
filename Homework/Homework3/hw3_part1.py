"""This program takes a input of a paragraph and calculates the average sentence length of the paragraph.
It also does other calcuations that help determine the complexity of the paragraph. Calculations include
the PHW, ASYL, GFRI, and the FKRI.

Author: Jimmy Chen
Version: 1
"""
from syllables import find_num_syllables

if __name__ == "__main__":
    paragraph = input("Enter a paragraph => ").strip()
    print(paragraph)

    # Split the paragraph into words and count the number of periods in the paragraph.
    words = paragraph.split()
    periods = paragraph.count('.')

    '''ASL = Average Sentence Length'''
    # Calculate the average sentence length of the paragraph. as length of words divided by number of periods.
    ASL = len(words)/periods


    '''PHW = Percentage of Hard Words'''
    # Count the number of hard words in the paragraph. Hard words are words with more than 3 syllables.
    hard_words = []
    for word in words:
        if find_num_syllables(word) >= 3 and word.count('-') == 0:
            if not word.endswith('es') and not word.endswith('ed'):
                hard_words.append(word)

    # Calculate the percentage of hard words in the paragraph.
    PHW = len(hard_words)/len(words) * 100

    '''ASYL = Average Num of Syllables'''
    # Calculate the average number of syllables per word in the paragraph.
    total_syllables = 0
    for word in words:
        total_syllables += find_num_syllables(word)

    ASYL = total_syllables/len(words)

    '''GFRI = Gunning Fog Readability Index'''
    # Calculate the Gunning Fog Readability Index of the paragraph.
    GFRI = 0.4 * (ASL + PHW)

    '''FKRI = Flesch-Kincaid Readability Index'''
    # Calculate the Flesch-Kincaid Readability Index of the paragraph.
    FKRI = (206.835 - 1.015 * ASL) - (86.4 * ASYL)

    # Print the results
    print('Here are the hard words in this paragraph:')
    print(hard_words)
    print('Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}'.format(ASL, PHW, ASYL))
    print('Readability index (GFRI): {:.2f}'.format(GFRI))
    print('Readability index (FKRI): {:.2f}'.format(FKRI))