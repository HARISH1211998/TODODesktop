filepath1 = "todo.txt"
def getTodos(filepath=filepath1):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def putTodos(todos, filepath=filepath1):
    with open(filepath, 'w') as file:
        file.writelines(todos)