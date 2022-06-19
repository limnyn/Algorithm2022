# https://shoark7.github.io/programming/algorithm/4-ways-to-get-subarray-consecutive-sum


test_case = [[2],
             [-1],
             [-2, 1, -2],
             [1,2,3,4,5],
             [-3, -4, -5, -2, -1, 0],
             [3, 2, -6, 4, 0],
             [100, -100, 50, -50, 1000],
             [-1000, -1000, -1000, -1000],
             [1, 2, -1, 15, 0, 5, 1000, -1000],
             [-2, -3, 4, -1, -2, 1, 5, -3],
	     [-1, -2, -3],
            ]
ans = [1, 2, -1, 15, 0, 5, 1000, -1000, 1022, 7]
functions = [exhaustive_search, partial_sum,
             divide_conquer, dynamic_programming]


for func in functions:
    print('Function is', func.__name__)
    for i in range(len(test_case)):
        try:
            assert cumulative(test_case[i]) == ans[i]
        except:
            print('test_case is', test_case[i], 'and ans is', ans[i], \
                  '.. but i got', max_consecutive_sum(test_case[i]))

# 답의 하한선보다 작은 MIN 지정
MIN = -2 ** 31 - 1


def exhaustive_search(arr):
    N = len(arr)

    def find(now, tmp_ans):
        if now == N:
            return MIN

        ans = max(arr[now], # 1.
                  tmp_ans + arr[now], # 2.
                  find(now + 1, arr[now]), # 3.
                  find(now + 1, tmp_ans + arr[now])) # 4.
        return ans

    return find(0, 0)


def partial_sum(arr):
    # 1.
    arr = [0] + arr
    N = len(arr)
    p_sum = [0] * N
    ans = MIN

    # 2.
    for i in range(1, N):
        p_sum[i] = p_sum[i-1] + arr[i]

    # 3.
    for hi in range(1, N):
        for lo in range(1, hi+1):
            ans = max(ans, p_sum[hi] - p_sum[lo-1])

    return ans


def divide_conquer(arr):
    N = len(arr)

    def find(lo, hi):
        # 1.
        if lo == hi:
            return arr[lo]

        mid = (lo + hi) // 2
	# 2.
        left = find(lo, mid)
        right = find(mid+1, hi)

        # 3.
        tmp = 0
        left_part = MIN
        for i in range(mid, lo-1, -1):
            tmp += arr[i]
            left_part = max(left_part, tmp)

        tmp = 0
        right_part = MIN
        for i in range(mid+1, hi+1):
            tmp += arr[i]
            right_part = max(right_part, tmp)

        # 4.
        return max(left, right, left_part + right_part)

    # 5.
    return find(0, N-1)


def dynamic_programming(arr):
    cache = [None] * len(arr)
    # 1.
    cache[0] = arr[0]

    # 2.
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]

    return max(cache)
