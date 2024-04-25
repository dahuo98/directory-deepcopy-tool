import os
import shutil


def ask_to_proceed():
    answer = input("Continue? (y/n) \n")

    if answer.lower() in ["y","yes"]:
        return
    elif answer.lower() in ["n","no"]:
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

"""
Copies the source file to the destination directory

Args:
    source_path: path to source file, must be an existing file
    dest_path: path of destination directory, must be a directory path, directory will be created if not present
    
Returns:
    int: number of bytes copied
"""
def copy_file(source_path: str, dest_path: str) -> int:
    if not os.path.isfile(source_path):
        print("ERROR: {path} is not a file!".format(path = source_path))
        exit(1)

    if os.path.isfile(dest_path):
        print("ERROR: {path} already exists and is a file!".format(path = dest_path))
        exit(1)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    shutil.copy(source_path, dest_path)
    num_bytes_copied = os.path.getsize(source_path)
    return num_bytes_copied



if __name__ == '__main__':

    # source_path = get_directory_path_from_commandline("source path: \n")
    # destination_path = get_directory_path_from_commandline("destination path: \n")
    source_path = input("source path: \n")
    destination_path = input("destination path: \n")
    print("copying {source} to {dest}".format(source=source_path, dest=destination_path))
    copy_file(source_path, destination_path)


