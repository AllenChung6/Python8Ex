import os
import logging
from file_reader import process_file

# abs path : /Users/allenc/PyCharmProjects/Python8Ex/dir1

print(os.path.abspath('dir1'))


def write_path_file(file_path):
    # the absolute file path parameter
    file_path = os.path.abspath(file_path)

    try:
        if os.path.exists(file_path):
            print('The file already exists')
        else:
            with open(file_path, 'w') as f:
                f.write(f'{file_path}')
                print("You have created a file.")
                f.close() if f else logging.warning("No file resource available to close.")
    except OSError as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)


# writes the absolute file path to a new file in the specified directory
write_path_file('dir1/file1.txt')
