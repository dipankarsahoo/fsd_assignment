# Write a Python script to extract book data from a bookfile using pickle. Also print
# extracted book data.

import pickle

def decode_data_file(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
        for key, value in data.items():
            print(key, ':', value)
        
decode_data_file('bookfile.txt')