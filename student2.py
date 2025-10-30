# 학생 정보를 저장할 딕셔너리
students = {}

# 1. 학생 추가 함수
def add_student():
    name = input("이름을 입력하세요: ").strip()  # 이름 입력 받기
    # 이미 학생이 등록되어 있는지 확인
    if name in students:
        print(f"{name} 학생은 이미 등록된 학생입니다. 다른 이름을 입력해주세요.")
        return
    # 나이 입력 받기
    try:
        age = int(input("나이를 입력하세요: "))
        students[name] = age  # 딕셔너리에 학생 추가
        print(f"{name} 학생이 추가되었습니다!")
    except ValueError:
        print("나이는 숫자만 입력 가능합니다. 다시 시도해주세요.")

# 2. 학생 목록 보기 함수
def show_students():
    if not students:  # 학생 목록이 비어있는지 확인
        print("등록된 학생이 없습니다.")
    else:
        print("등록된 학생 목록:")
        for name, age in students.items():
            print(f"{name}: {age}세")

# 3. 메뉴 실행 함수
def menu():
    while True:
        # 메뉴 출력
        print("""\n1. 학생 추가
2. 학생 목록 보기
3. 종료""")
        
        try:
            choose_number = int(input("번호를 선택하세요: "))
        except ValueError:
            print("잘못된 입력입니다. 번호는 숫자만 입력 가능합니다.")
            continue
        
        # 메뉴 번호에 맞는 기능 실행
        if choose_number == 1:
            add_student()  # 학생 추가
        elif choose_number == 2:
            show_students()  # 학생 목록 보기
        elif choose_number == 3:
            print("프로그램을 종료합니다.")
            break  # 종료
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")  # 잘못된 번호 입력 시

# 프로그램 시작
if __name__ == "__main__":
    menu()  # 메뉴 함수 실행
