"""
This program decrypts and encrypts a word using a simple ruleset in the homework file.
Then, it checks if the operation of decrypting and encrypting the word is the same as the original word.
If it is, the operation is reversable on the string.

Author: Jimmy Chen
Version: 1
"""

def encrypt(word):
    # This function encrypts the word using the ruleset in the homework file.
    word = word.replace(' a', '%4%')
    word = word.replace('he', '7!')
    word = word.replace('e', '9(*9(')
    word = word.replace('y', '*%$')
    word = word.replace('u', '@@@')
    word = word.replace('an', '-?')
    word = word.replace('th', '!@+3')
    word = word.replace('o', '7654')
    word = word.replace('9', '2')
    word = word.replace('ck', '%4')
    return word

def decrypt(word):
    # This function decrypts the encrypted word using the ruleset in the homework file.
    # It is the reverse of the encrypt function.
    word = word.replace('%4', 'ck')
    word = word.replace('2', '9')
    word = word.replace('7654', 'o')
    word = word.replace('!@+3', 'th')
    word = word.replace('-?', 'an')
    word = word.replace('@@@', 'u')
    word = word.replace('*%$', 'y')
    word = word.replace('9(*9(', 'e')
    word = word.replace('7!', 'he')
    word = word.replace('%4%', ' a')
    return word

if __name__ == "__main__":
    # Ask the user for the word and convert it to the correct data type.
    word = input("Enter a string to encode ==> ").strip()
    print(word, "\n")

    # Encrypt the word, then decrypt it, and check if the decrypted word is the same as the original word.
    encrypted_word = encrypt(word)
    decrypted_word = decrypt(encrypted_word)
    is_reversable = word == decrypted_word

    # Find the difference in length between the original word and the encrypted word.
    difference_length = abs(len(word) - len(encrypted_word))

    # Print the results of the encryption and decryption.
    print("Encrypted as ==> {}".format(encrypted_word))
    print("Difference in length ==> {}".format(difference_length))
    print("Deciphered as ==> {}".format(decrypted_word))

    if word == decrypted_word:
        print("Operation is reversible on the string.")
    else:
        print("Operation is not reversible on the string.")
