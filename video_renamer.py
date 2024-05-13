
import os, re, datetime


BAD_DATE_PATTERN = r"\d\d-\d\d-\d\d\d\d"
GOOD_DATE_PATTERN = r"\d\d\d\d-\d\d-\d\d"
VALID_FILE_EXTENSIONS = ('.mkv', '.mp4')


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

# renames files with the bad date format
# returns the new filename or the old name if no change was needed
def fix_bad_date_format(parent_dir_path: str, filename: str) -> None:
    old_path = os.path.join(parent_dir_path, filename)
    
    date_match = re.search(BAD_DATE_PATTERN, filename)
    if not date_match:
        return
    reformatted_date = year_to_front(date_match.group())
    
    reformatted_name = filename.replace(date_match.group(), reformatted_date)
    new_path = os.path.join(parent_dir_path, reformatted_name)
    
    os.rename(old_path, new_path)

# adds a file's creation date to its name if it isn't already there
# returns the new filename or the old name if no change was needed
def add_date_to_filename(parent_dir_path: str, filename: str) -> None:
    old_path = os.path.join(parent_dir_path, filename)
    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(old_path))
    name_with_date = f'{creation_time.date()} {filename}'
    new_path = os.path.join(parent_dir_path, name_with_date)
    
    os.rename(old_path, new_path)

if __name__ == '__main__':
    path_to_search = get_file_path()
    # path_to_search = 'test_files'
    for dirpath, dirnames, filenames in os.walk(path_to_search):
        for filename in filenames:
            if not filename.endswith(VALID_FILE_EXTENSIONS):
                continue
            
            if not re.search(GOOD_DATE_PATTERN, filename):
                add_date_to_filename(dirpath, filename)
            
            fix_bad_date_format(dirpath, filename)
            
            # TODO: find duplicate files of different type
