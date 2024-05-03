import os
import shutil


def ask_to_proceed():
    answer = input("Continue? (y/n) \n")

    if answer.lower() in ["y", "yes"]:
        return
    elif answer.lower() in ["n", "no"]:
        exit(1)
    else:
        exit(1)


def get_directory_path_from_commandline(prompt: str) -> str:
    path = input(prompt)
    print("got path: {dir_path}".format(dir_path=path))
    files = os.listdir(path)
    print("current files under this directory: ")
    print("count: {n} files".format(n=len(files)))
    for file in files:
        print(file)
    ask_to_proceed()
    return path


def check_destination_file_exists(source_file_path: str, dest_directory_path: str) -> None:
    base_file_name = os.path.basename(source_file_path)
    dest_file_path = os.path.join(dest_directory_path, base_file_name)

    if os.path.exists(dest_file_path):
        print("destination file {dest_file} already exists, continue will overwrite".format(dest_file=dest_file_path))
        ask_to_proceed()


"""
Copies the source file to the destination directory

Args:
    source_path: path to source file, must be an existing file
    dest_path: path of destination directory, must be a directory path, directory will be created if not present
    
Returns:
    int: number of bytes copied
"""


def copy_file(source_path: str, dest_path: str) -> int:
    print("copying file {source} to {dest}".format(source=source_path, dest=dest_path))

    if not os.path.isfile(source_path):
        print("ERROR: {path} is not a file!".format(path=source_path))
        exit(1)

    if os.path.isfile(dest_path):
        print("ERROR: {path} already exists and is a file!".format(path=dest_path))
        exit(1)

    check_destination_file_exists(source_path, dest_path)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    shutil.copy(source_path, dest_path)
    num_bytes_copied = os.path.getsize(source_path)
    return num_bytes_copied


"""
Copy all content under source_directory_path to under dest_directory_path.

Content will be merged into dest_directory_path. That is when copying source directory to destination directory,
the file structure will be preserved. Furthermore, if destination directory already exists, file will be put under
the desire directory instead of overwrite the entire directory

Args:
    source_directory_path: path to source directory
    dest_directory_path: path of destination directory
    
Returns:
    int: number of bytes copied

example:
source: /common/path/path/to/file.txt
destination: /common/path/

destination before copy:
|--common
|    |
|    |--path
|    |    |
|    |    |-path
|    |    |   |
|    |    |   |--to
|    |    |   |   |
|    |    |   |   |--old_file1.txt
|    |    |   |   |--old_file2.txt

-----------------------------------------------------

destination after copy:
|--common
|    |
|    |--path
|    |    |
|    |    |-path
|    |    |   |
|    |    |   |--to
|    |    |   |   |
|    |    |   |   |--old_file1.txt
|    |    |   |   |--old_file2.txt
|    |    |   |   |--file.txt
"""


def merge_copy_directory(source_directory_path: str, dest_directory_path: str) -> int:
    print('merge copying directory {source} to {dest}'.format(source=source_directory_path, dest=dest_directory_path))

    for source_entry_name in os.listdir(source_directory_path):

        abs_source_entry_path = os.path.join(source_directory_path, source_entry_name)
        abs_dest_entry_path = os.path.join(dest_directory_path, source_entry_name)

        if os.path.isfile(abs_source_entry_path):
            copy_file(abs_source_entry_path, dest_directory_path)
        elif os.path.isdir(abs_source_entry_path):
            merge_copy_directory(abs_source_entry_path, abs_dest_entry_path)
        else:
            print("should not be here")
            exit(1)


if __name__ == '__main__':
    source_path = get_directory_path_from_commandline("source path: \n")
    destination_path = get_directory_path_from_commandline("destination path: \n")
    merge_copy_directory(source_path, destination_path)
