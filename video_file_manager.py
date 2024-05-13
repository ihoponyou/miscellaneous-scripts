
import os
import re

# MM-DD-YYYY -> YYYY-MM-DD
def year_to_front(date: str) -> str:
    date_tokens = date.split('-')
    date_tokens.insert(0, date_tokens.pop())
    return '-'.join(date_tokens)

def get_file_path() -> str:
    input_path = ''
    while not os.path.exists(input_path):
        input_path = input('Enter a file path: ')
    return input_path


bad_date_pattern = r"\d\d-\d\d-\d\d\d\d"
processed_file_names = {}

if __name__ == '__main__':
    path_to_search = get_file_path()
    # path_to_search = 'test_files'
    for root, dirs, files in os.walk(path_to_search):
        for name in files:
            if not name.endswith(('.mkv', '.mp4')):
                continue

            date_match = re.search(bad_date_pattern, name)
            if not date_match:
                continue
            reformatted_date = year_to_front(date_match.group())
            
            # print(name.replace(date_match.group(), reformatted_date))
            old_path = os.path.join(root, name)
            new_path = os.path.join(root, name.replace(date_match.group(), reformatted_date))
            os.rename(old_path, new_path)
            
            # find duplicate files of different type
