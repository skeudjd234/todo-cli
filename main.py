import todo
import save

todos = save.load_todos()

def get_id():
    try:
        todo_id = int(input("To-do id를 입력하세요: "))
        return todo_id
    except ValueError:
        print("숫자를 입력해주세요.")
        return None
while True:
    print("\n============ To-do List ============")
    print("\n1. 항목 추가")
    print("\n2. 항목 조회")
    print("\n3. 완료 표시")
    print("\n4. 항목 삭제")
    print("\n5. 타이틀 변경")
    print("\n6. 저장하기")
    print("\n7. 종료하기")
    program_do = input("\n당신의 선택: ")

    if program_do == "1":
        title = input("\n추가할 일: ")
        todo.add_todo(todos, title)

    elif program_do == "2":
        todo.show_todos(todos)

    elif program_do == "3":
        todo_id = get_id()

        if todo_id is not None:
            todo.complete_todo(todos, todo_id)
    elif program_do == "4":
        todo_id = get_id()

        if todo_id is not None:
            todo.delete_todo(todos, todo_id)
    elif program_do == "5":
        todo_id = get_id()
        if todo_id is not None:
            new_title = input("새 타이틀을 입력하세요: ")
            todo.update_todo(todos, todo_id, new_title)
    elif program_do == "6":
        save.save_todos(todos)
    elif program_do == "7":
        to_save = input("\n종료 전에 저장하시겠습니까? 예/아니오로 대답: ").strip()
        if to_save == "예":
            save.save_todos(todos)
            break
        else:
            break
    else:
        print("1 ~ 7 중에서 올바른 숫자를 입력해주세요.")