import json

def save_todos(todos):
    with open("todos.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=4, ensure_ascii=False)
    print("\n저장 완료!")

def load_todos():
    try:
        with open("todos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []