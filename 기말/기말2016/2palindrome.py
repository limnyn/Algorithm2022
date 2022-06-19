# 입력으로 영문 대문자로 구성된 하나의 문자열을 받아서 가장 긴 paliindrome인 부분 문자열의 길이를 구하는 프로그램을 작성하라.
# BBABCBCAB => BABCBAB, 부분 문자열이면서 가장긴 palindrome
#                 BBBBB나 BBCBB도 palindrome이지만 가장 길진 않음

# 가장 긴 회문 부분 수열의 길이를 찾는 함수
# 하위 문자열 `X[i…j]`의
# 가장 긴 회문 부분 수열의 길이를 찾는 함수
# 하위 문자열 `X[i…j]`의
def findLongestPalindrome(X, i, j, lookup):
 
    # 기본 조건
    if i > j:
        return 0
 
    # 문자열 `X`에 하나의 문자만 있으면 회문입니다.
    if i == j:
        return 1
 
    #는 입력의 동적 요소에서 고유 키를 구성합니다.
    key = (i, j)
 
    # 하위 문제가 처음 발견되면 해결하고
    # 결과를 사전에 저장
    if key not in lookup:
 
        ''' If the last character of the string is the same as the first character,
            include the first and last characters in palindrome and recur
            for the remaining substring X[i+1, j-1] '''
 
        if X[i] == X[j]:
            lookup[key] = findLongestPalindrome(X, i + 1, j - 1, lookup) + 2
        else:
            ''' If the last character of the string is different from the
                first character
 
                1. Remove the last character recur for the remaining substring
                   `X[i, j-1]`
                2. Remove the first character recur for the remaining substring
                   `X[i+1, j]`
                3. Return the maximum of the two values '''
 
            lookup[key] = max(findLongestPalindrome(X, i, j - 1, lookup),
                            findLongestPalindrome(X, i + 1, j, lookup))
 
    # 사전에서 하위 문제 솔루션을 반환합니다.
    return lookup[key]
 
 
if __name__ == '__main__':
 
    X = 'BBABCBCAB'
 
    #는 하위 문제에 대한 솔루션을 저장하는 사전을 만듭니다.
    lookup = {}
 
    print('The length of the longest palindromic subsequence is',
        findLongestPalindrome(X, 0, len(X) - 1, lookup))
#  https://www.techiedelight.com/ko/longest-palindromic-subsequence-using-dynamic-programming/



# 아래는 인쇄까지
# # `X[0…m-1]`과 `Y[0…n-1]`의 LCS를 찾는 함수
# def findLongestPalindrome(X, Y, m, n, lookup):
 
#     #는 시퀀스의 끝에 도달하면 빈 문자열을 반환합니다.
#     if m == 0 or n == 0:
#         return ""
 
#     # `X`와 `Y`의 마지막 문자가 일치하는 경우
#     if X[m - 1] == Y[n - 1]:
 
#         # 현재 문자(`X[m-1]` 또는 `Y[n-1]`)를 LCS에 추가
#         # 하위 문자열 `X[0…m-2]` 및 `Y[0…n-2]`
#         return findLongestPalindrome(X, Y, m - 1, n - 1, lookup) + X[m - 1]
 
#     # 그렇지 않으면 `X`와 `Y`의 마지막 문자가 다른 경우
 
#     # 현재 셀의 맨 위 셀이 왼쪽보다 더 큰 값을 가지고 있는 경우
#     # 셀, 문자열 `X`의 현재 문자를 삭제하고 LCS 찾기
#     # 하위 문자열 `X[0…m-2]`, `Y[0…n-1]`의
 
#     if lookup[m - 1][n] > lookup[m][n - 1]:
#         return findLongestPalindrome(X, Y, m - 1, n, lookup)
 
#     # 현재 셀의 왼쪽 셀이 상단보다 더 큰 값을 가지고 있는 경우
#     # 셀, 문자열 `Y`의 현재 문자를 삭제하고 LCS 찾기
#     # 하위 문자열 `X[0…m-1]`, `Y[0…n-2]`의
 
#     return findLongestPalindrome(X, Y, m, n - 1, lookup)
 
 
# # 하위 문자열 `X[0…n-1]` 및 `Y[0…n-1]`의 LCS 길이를 찾는 함수
# def LCSLength(X, Y, n, lookup):
 
#     # 룩업 테이블을 상향식으로 채웁니다.
#     # 조회 테이블의 첫 번째 행과 첫 번째 열이 이미 0입니다.
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             # 'X'와 'Y'의 현재 문자가 일치하는 경우
#             if X[i - 1] == Y[j - 1]:
#                 lookup[i][j] = lookup[i - 1][j - 1] + 1
 
#             # 그렇지 않으면 `X`와 `Y`의 현재 문자가 일치하지 않는 경우
#             else:
#                 lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
#     return lookup[n][n]
 
 
# if __name__ == '__main__':
 
#     X = 'ABBDCACB'
 
#     # 문자열 'Y'는 'X'의 반대입니다.
#     Y = X[::-1]
 
#     # lookup[i][j]는 하위 문자열 `X[0…i-1]` 및 `Y[0…j-1]`의 LCS 길이를 저장합니다.
#     lookup = [[0 for x in range(len(X) + 1)] for y in range(len(X) + 1)]
 
#     # LCS를 사용하여 LPS의 길이 찾기
#     print('The length of the longest palindromic subsequence is',
#         LCSLength(X, Y, len(X), lookup))
 
#     # 조회 테이블을 사용하여 LPS 인쇄
#     print('The longest palindromic subsequence is',
#         findLongestPalindrome(X, Y, len(X), len(X), lookup))
 