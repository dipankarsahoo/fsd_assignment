# Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or
# not

import re

def search_city_in_file(filename, city):
    with open(filename, 'r') as f:
        lines = f.readlines()
        line_count = 0
        for line in lines:
            line_list = line.split(' ')
            word_count = 0
            line_count += 1
            for word in line_list:
                word_count += 1
                # This is a regex substitution to remove any special characters attached to the word. Now word can contain only alphanumeric characters.
                if city == re.sub('[^A-Za-z0-9]+', '', word):
                    return (line_count, word_count)
        return None
    
print(search_city_in_file('cities.txt', 'Bangalore') )          