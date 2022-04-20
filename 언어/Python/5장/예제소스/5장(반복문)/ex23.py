# 사용자로부터 전화번호를 입력받다 보면 "-"를 적는 경우가 많다.
# "-"을 합하여 입력받도록 하고 출력을 할 때는 "-"삭제를 한 문자열을 출력하는
# 프로그램을 작성하시오.

phone_num = input("당신의 전화번호를 입력하세요.(-포함) : ")
new_phone_num = ""

# 010-111-1111 이거나 010-1111-1111
if len(phone_num) == 12 or len(phone_num) == 13:
    for ch in phone_num:
        # 루프문자가 "-"아니라면 참을 반환한다.
        if ch != "-":
            new_phone_num += ch
    print("'-'를 제거한 전화번호 : " + new_phone_num)
else:
    print("전화번호 입력이 잘못되었습니다.")


