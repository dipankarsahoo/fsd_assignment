# Write a Python script to count the number of Python keywords occurring in a python
# source file.

import token
import keyword
import tokenize

def find_number_of_keywords_in_py_file(filename):
    keywords = []
    with open(filename, 'r') as f:
        count = 0
        for line in tokenize.generate_tokens(f.readline):
            if line.type == token.NAME and keyword.iskeyword(line.string):
                count += 1
                keywords.append(line.string)
        
    return (count, keywords)

print(find_number_of_keywords_in_py_file("C:\Python projects\My Proj\\fsd_assignment\Assignment_29\six_29.py"))