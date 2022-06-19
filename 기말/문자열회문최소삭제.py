# https://www.techiedelight.com/ko/find-minimum-number-deletions-convert-string-into-palindrome/

# 문자열을 회문으로 만들기 위한 최소 삭제횟수
# 삭제에 필요한 최소 삭제 횟수를 찾는 기능
# 주어진 문자열 `X[0…n-1]`을 회문으로 변환
def minDeletions(X):
 
    n = len(X)
 
    # 문자열 'Y'는 'X'의 반대입니다.
    Y = X[::-1]
 
    # `lookup[i][j]`는 하위 문자열 `X[0…i-1]` 및 `Y[0…j-1]`의 LCS 길이를 저장합니다.
    lookup = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    # 상향식 방식으로 조회 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 'X'와 'Y'의 현재 문자가 일치하는 경우
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
 
            # 그렇지 않으면 'X'와 'Y'의 현재 문자가 일치하지 않는 경우
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
    # 이제 `lookup[n][n]`은 가장 긴 회문 부분 시퀀스의 크기를 포함합니다.
 
    # 필요한 최소 삭제 횟수는 크기의 차이입니다.
    # 문자열의 # 및 회문 하위 시퀀스의 크기
 
    return n - lookup[n][n]
 
 
if __name__ == '__main__':
 
    X = 'ACBCDBAA'
 
    print('The minimum number of deletions required is', minDeletions(X))