import os

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


if __name__ == '__main__':

    source_path = get_directory_path_from_commandline("source path: \n")
    destination_path = get_directory_path_from_commandline("destination path: \n")


