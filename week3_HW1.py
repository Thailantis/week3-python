# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups 
# (return None for names with no first and last name, or names that aren't properly capitalized)
# Hint: use with open() and readlines()
# """
# Expected Output
# Abraham Lincoln
# Andrew P Garfield
# Connor Milliken
# Jordan Alexander Williams
# None
# None
# """

import re

with open("regex_test.txt", "r") as file:
    for line in file:
        match = re.search(r"\b[A-Z][a-z]*\s[A-Z][a-z]*\b", line)
        if match:
            print(match.group())
        else:
            print(None)
