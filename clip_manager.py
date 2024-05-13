
import os, re, datetime


BAD_DATE_PATTERN = r"\d\d-\d\d-\d\d\d\d"
GOOD_DATE_PATTERN = r"\d\d\d\d-\d\d-\d\d"
VALID_FILE_EXTENSIONS = ('.mkv', '.mp4')
DELETE_DUPLICATE_CLIPS = True


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
def fix_bad_date_format(parent_dir_path: str, filename: str, matched_date: re.Match) -> str:
    old_path = os.path.join(parent_dir_path, filename)
    reformatted_date = year_to_front(matched_date.group())
    reformatted_name = filename.replace(matched_date.group(), reformatted_date)
    new_path = os.path.join(parent_dir_path, reformatted_name)
    
    os.rename(old_path, new_path)
    return reformatted_name

# adds a file's creation date to its name if it isn't already there
# returns the new filename or the old name if no change was needed
def add_date_to_filename(parent_dir_path: str, filename: str) -> str:
    old_path = os.path.join(parent_dir_path, filename)
    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(old_path))
    name_with_date = f'{creation_time.date()} {filename}'
    new_path = os.path.join(parent_dir_path, name_with_date)
    
    os.rename(old_path, new_path)
    return name_with_date


if __name__ == '__main__':
    path_to_traverse = get_file_path()
    processed_filenames = {}
    for dirpath, dirnames, filenames in os.walk(path_to_traverse):
        for filename in filenames:
            if not filename.endswith(VALID_FILE_EXTENSIONS):
                continue

            working_name = filename
            
            bad_date_match = re.search(BAD_DATE_PATTERN, filename)
            if bad_date_match:
                working_name = fix_bad_date_format(dirpath, filename, bad_date_match)

            if not (bad_date_match or re.search(GOOD_DATE_PATTERN, filename)):
                working_name = add_date_to_filename(dirpath, filename)
            
            abs_path_no_extension = os.path.join(dirpath, working_name[:-4])
            try:
                processed_filenames[abs_path_no_extension] += 1
            except:
                processed_filenames[abs_path_no_extension] = 1

    if DELETE_DUPLICATE_CLIPS:    
        # some clips were auto-remuxed from .mkv to .mp4
        # and i didnt clean them out
        for filename, copies in processed_filenames.items():
            if copies < 2:
                continue
            mp4_path = f'{filename}.mp4'
            os.remove(mp4_path) # this is scary
