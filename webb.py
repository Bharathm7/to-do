import streamlit as st;
import function;

if 'new_todo' not in st.session_state:
    st.session_state.new_todo = ""



def addtodo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todo(todos)


todos = function.get_todo();

st.text("todoapp")
st.subheader("my todo app")
st.write("used for writing my todo app")

for i, todo in enumerate(todos):
    checkbox_state = st.checkbox(f"{i + 1}. {todo}")
    if checkbox_state:
        todos.pop(i)
        function.write_todo(todos)
        del st.session_state["new_todo"]
        st.experimental_rerun()

st.text_input(label="", placeholder="enter todo", on_change=addtodo, key="new_todo")
