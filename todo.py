def find_todo(todos, id):
    for item in todos:
        if item["id"] == id:
            return item
        
    print("올바른 id를 입력하세요.")
    return None

def add_todo(todos, title):
    max_id = 0
    new_todo = {}

    for item in todos:
        if item["id"] > max_id:
            max_id = item["id"]

    new_todo["id"] = max_id + 1
    new_todo["title"] = title
    new_todo["done"] = False

    todos.append(new_todo)

def show_todos(todos):
    if not todos:
        print("등록된 할 일이 없습니다.")
        return
    for item in todos:
        if item["done"] == False:
            to_print = "미완료"
        elif item["done"] == True:
            to_print = "완료"
        print(f'\n{item["id"]}. 할 일: {item["title"]} 완료 여부: {to_print}')

def complete_todo(todos, id):
    todo = find_todo(todos, id)

    if todo is not None:
        todo["done"] = True

def delete_todo(todos, id):
    todo = find_todo(todos, id)

    if todo is not None:
        todos.remove(todo)

def update_todo(todos, id, new_title):
    todo = find_todo(todos, id)

    if todo is not None:
        todo["title"] = new_title