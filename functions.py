from os import PathLike
from typing import List
FILEPATH = "/home/Todo_App/todos.txt"

def get_todos(filepath: PathLike = FILEPATH) -> List[str]:
    """Read a text file and return the list of to-do items"""
    
    with open(filepath, "r") as file_local:
        return file_local.readlines()
    
def write_todos(todos_arg: List[str], filepath: PathLike = FILEPATH) -> None:
    """Write a list of to-do items list in a text file"""
    
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)