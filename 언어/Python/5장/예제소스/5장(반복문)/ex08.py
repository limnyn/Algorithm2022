# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

num = int(input("출력하고 싶은 단을 입력하세요(2~9) : "))

for i in range(1, 10):
    # 사용자의 잘못된 입력을 걸러내는 방법
    if (num < 2) or (num > 9):
        print("단을 잘못 입력하셨습니다.")
        break
    print(num, "*", i, "=", (num*i))

