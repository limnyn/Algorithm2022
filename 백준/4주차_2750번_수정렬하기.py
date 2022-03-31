# 수 정렬하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	117086	66734	46187	58.393%
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5


n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

def sorting(arr,n):
    for i in range(n):
        for j in range(n-1):
            if  arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


sorting(num,n)
for i in range(n):
    print(num[i])