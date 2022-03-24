# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 10 초	128 MB	60887	30215	19832	49.049%
# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# 예제 입력 1 
# 8
# 예제 출력 1 
# 92
import sys
sys.setrecursionlimit(1000000)
global countWay
countWay = 0

n = int(input())
cols = []
for _ in range(n+1):
    cols.append(0)

def promising(level):
    for i in range(1,level):
        if(cols[i]==cols[level]):
            return False
        elif (level - i == abs(cols[level]-cols[i])):
            return False

    return True

def queens(level):
    global countWay
    if (promising(level)==False):
        return False

    elif level == n:
        # for i in range(1,n+1):
        #     print(cols[i], end=" ")
        # print()
        countWay+=1
        return False

    for i in range(1,n+1):
        cols[level+1] = i
        if queens(level+1):
            return True

    return False
        

queens(0)
print(str(countWay))