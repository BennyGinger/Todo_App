import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"]
    todos = functions.get_todos()
    todos.append(todo+"\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("Add and create a simple list of todos")
st.write("Enter a todo in the box below and click the 'Add' button to add it to the list.\
    Check the box when completed to remove it from the list.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        
    
st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo",)

# st.session_state