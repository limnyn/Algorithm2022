# 입력으로 영문 대문자로 구성된 두 문자열을 받아서 두 문자열을 포함하는 가장 짧은 문자열의 길이를 구하여 
# 출력하는 프로그램을 작성하라.
# LCS 문제이다

# 입력 예
#     7
#     ABCBDAB
#     6
#     BDCABA

# 출력 예 
#     8


# 길이반환 ==  두 문자열의 길이 합 - 겹치는 최장 공통 부분 문자열(LCS)

a = '0'+input()
b = '0'+input()
a_len = len(a)
b_len = len(b)
dplist = []
for i in range(b_len):
    lst = []
    for j in range(a_len):
        lst.append(0)
    dplist.append(lst)


# 바텀업
# for i in range(b_len):
#     for j in range(a_len):
#         if i == 0 or j == 0:
#             dplist[i][j] == 0
#         elif b[i] == a[j]:
#             dplist[i][j]= dplist[i-1][j-1] + 1
#         else:
#             dplist[i][j] = max(dplist[i-1][j],dplist[i][j-1])

# print(dplist[b_len-1][a_len-1])


#탑다운
def dp(i, j):
    if i == 0 or j == 0:
        dplist[i][j] == 0
    elif b[i] == a[j]:
        dplist[i][j]= dp(i-1,j-1) + 1
    else:
        dplist[i][j] = max(dp(i-1,j),dp(i,j-1))
    if i == b_len-1 and j == a_len-1:
        print(i+j-dplist[i][j])
        return 0
    return dplist[i][j]

dp(b_len-1,a_len-1)

# print(dp(b_len-1,a_len-1))



# 최장 공통 부분 수열(또는 문자열) 
# # for i in range(b_len):
# #     for j in range(a_len):
# #         if i == 0 or j == 0:
# #             dplist[i][j] == 0
# #         elif b[i] == a[j]:
# #             dplist[i][j]= dplist[i-1][j-1] + 1
# #         else:
# #             dplist[i][j] = max(dplist[i-1][j],dplist[i][j-1])

# ABCDEF
# GBCDFE
# =BCDF

# 최장공통 수열(문자열)
# # for i in range(b_len):
# #     for j in range(a_len):
# #         if i == 0 or j == 0:
# #             dplist[i][j] == 0
# #         elif b[i] == a[j]:
# #             dplist[i][j]= dplist[i-1][j-1] + 1
# #         else:
# #             dplist[i][j] = 0


# ABCDEF
# GBCDFE
# =BCD
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-dplist-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence