# 길이가 N인 막대기가 있다. 이 막대기를 적당한 길이의 여러 개의 조각으로 잘라서 팔려고 한다. 단, 잘라진 막
# 대기 조각들의 길이는 모두 정수여야 한다. 막대기의 가격은 막대기의 길이에 따라 다르며, 막대기의 길이에 비
# 례하지는 않는다. 1에서 N사이의 모든 정수 K에 대해서 길이가 K인 막대기의 가격[vi | i = 1, 2, ..., N]이 입력
# 으로 주어진다. 주어진 막대기를 어떻게 잘라서 팔아야 가격의 합이 최대가 되는지 계산하는 순환식을 고안하
# 라. 예를 들어 N=8이고 가격이 아래의 표와 같다면 길이가 2와 6인 2개의 조각으로 자르는 것이 최선이며,
# 이때 가격의 합은 5+17 = 22이다. 




def cutRod(price, n):
  	# val : optimal value
    # 0으로 초기화 
    val = [0 for x in range(n+1)]
    for i in range(1, n+1):
        max_val = -1
        for j in range(i):
          	if max_val < price[j] + val[i-j-1]:
                  max_val = price[j] + val[i-j-1]
        val[i] = max_val
    return val[n]

vi = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(vi)
print("Maximum Obtainable Value is " + str(cutRod(vi, n)))