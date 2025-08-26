import student1, student2, student3

def main():
    students = {
        1: student1.student1,
        2: student2.student2,
        3: student3.student3
    }

    while True:
        command = int(input("작동 코드를 실행해주세요 : (0:종료/1~3:수강생 호출) ").strip())
        if command == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            students.get(command, lambda: print("잘못된 명령어입니다."))()

if __name__ == "__main__":
    main()
