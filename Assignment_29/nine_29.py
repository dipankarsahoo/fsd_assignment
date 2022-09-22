# Write a Python script to store book data in a file. Book data is in the form of a
# dictionary in which book name is the key and price is its value. Use pickle to store
# data into a file (say bookfile)

import pickle

data = {'Jungle Book': 250 , '1984': 100 , 'Being and Nothingness': 600 , 'Meditations': 100, 'Deep work': 200}

def encode_data_file(data):
    with open('bookfile.txt', 'ab') as f:
        pickle.dump(data, f)
        
encode_data_file(data)