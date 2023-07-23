import streamlit as st
import function

# Load existing todos from file
todos = function.getTodos()

def addtodo():
    todo = st.session_state.newtodo
    todos.append(todo)
    function.putTodos(todos, filepath="todo.txt")
    st.session_state.newtodo = ""
    st.experimental_rerun()

st.title("MY website First web port")
st.subheader("Select what you want to do")

# Use a copy of the todos list to avoid modifying the list while iterating
for todo in todos.copy():
    checkbox = st.checkbox(todo)
    if checkbox:
        todos.remove(todo)
        function.putTodos(todos, filepath="todo.txt")
        st.experimental_rerun()

# Use st.text_input directly, no need for an on_change callback
new_todo = st.text_input(placeholder="Enter the todo list you want", label="New Todo", key='newtodo')
if st.button("Add Todo"):
    if new_todo:
        addtodo()

# Display the newly created todos
for todo in st.session_state.newtodos:
    checkbox = st.checkbox(todo)
    if checkbox:
        st.session_state.newtodos.remove(todo)
        st.experimental_rerun()

# Combine the old todos with the newly created todos
combined_todos = todos + st.session_state.newtodos

# Save the combined todos to session state
st.session_state.newtodos = combined_todos
