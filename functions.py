from os import PathLike, getcwd
from os.path import exists, join
from typing import List

# Check if the file to store the to-do items exists
current_directory = getcwd()
file_path = join(current_directory,"todos.txt")
if not exists(file_path):
    with open("todos.txt", "w") as file_local:
        file_local.write("")

FILEPATH = file_path

def get_todos(filepath: PathLike = FILEPATH) -> List[str]:
    """Read a text file and return the list of to-do items"""
    
    with open(filepath, "r") as file_local:
        return file_local.readlines()
    
def write_todos(todos_arg: List[str], filepath: PathLike = FILEPATH) -> None:
    """Write a list of to-do items list in a text file"""
    
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)