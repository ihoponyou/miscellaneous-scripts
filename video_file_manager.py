
import os
import re

os.chdir("B:\\videos\\recordings")

bad_date_pattern = "\d\d-\d\d-\d\d\d\d"
processed_file_names = {}

for dir_path, dir_names, file_names in os.walk('.'):
    for f in file_names:
        if re.search(bad_date_pattern, f):
            split_by_space = f.split(' ')
            date_tokens = split_by_space[0].split('-')
            
            # move year to front
            date_tokens.insert(0, date_tokens.pop())
            reformatted_date = '-'.join(date_tokens)
            
            print(split_by_space[0], '->', reformatted_date)
            
        # find duplicate files of different type
