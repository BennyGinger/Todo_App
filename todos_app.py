import FreeSimpleGUI as fsg
from functions import get_todos, write_todos
import time

fsg.theme("Topanga")
time_stamp = fsg.Text("", key="time")
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter a to-do", key="todo")
list_box = fsg.Listbox(values=[todo.strip() for todo in get_todos()], 
                       size=(30, 10), key="todos", enable_events=True)
add_button = fsg.Button("Add")
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window("My to-do App", 
                    layout=[[time_stamp],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20),)

while True:
    event, values = window.read(timeout=10)
    if event is None:
        break
    window['time'].update(time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update([todo.strip() for todo in get_todos()])
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = get_todos()
                index = todos.index(todo_to_edit+"\n")
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update([todo.strip() for todo in get_todos()])
            except IndexError:
                fsg.popup("Please select a to-do to edit",font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete + "\n")
                write_todos(todos)
                window['todos'].update([todo.strip() for todo in get_todos()])
                window['todo'].update('')
            except IndexError:
                fsg.popup("Please select a to-do to complete",font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(values['todos'][0])
        case "Exit":
            break
        case fsg.WIN_CLOSED:
            break

window.close()
