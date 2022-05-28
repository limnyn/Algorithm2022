#201812177 이문현

# 1. rank 입력으로 N < 1000개의 정수 a1, a2, ... , an과 또 다른 하나의 정수 k가 주어진다.
# 정수들은 정렬되어 있지 않고, 동일한 값이 중복될 수도 있다. 
# 임의의 정수 x의 rank란 N개의 정수 a1, a2, ..., an중에서 x보다 작은 것의 개수 + 1을 말한다.
# 정수 K의 rank를 구해서 출력하는 프로그램을 작성하라. 
# 단, 처음에 입력 정수들을 읽어서 배열에 저장하는 부분을 제외하고 나머지 부분에서는 for문, while문 등의 반복문을 사용해서는 안된다.
# 입력의 형식은 먼저 정수의 개수 N이 주어지고, 이어서 N개의 정수가 주어진다.
# 마지막으로 정수 K가 주어진다. 시간복잡도가 O(N)을 초과해서는 안된다.

# 입력 예
# 10
# 2 5 3 8 6 7 8 7 2 1
# 8
# 출력
# 9


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 1

def islower(i,k,n):
    global count
    if(i==n):
        return
    if(arr[i] < k):
        islower(i+1, k,n)
        count+= 1
    else:
        islower(i+1, k, n)
        

islower(0,k,n)
print(count)