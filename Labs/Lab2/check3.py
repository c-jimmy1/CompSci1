string = input("Enter a word: ")

word_len = len(string)
line_len = word_len + 6

print("*" * line_len)
print("*" * 2, string, "*" * 2)
print("*" * line_len)