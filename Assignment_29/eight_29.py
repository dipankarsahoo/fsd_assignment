# Write a Python script to create a copy of a file.

import shutil

def create_file_copy(source_filename, dest_filename):
    shutil.copy(source_filename, dest_filename)
    
    
create_file_copy('myfile.txt', 'myfile_copied.txt')