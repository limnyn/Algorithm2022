# 2. [미로] 아래 그림과 같이 폭탄이 설치된 미로가 있다. 폭탄이 설치된 곳을 지나갈 수는 있지만 대신 부상을 당
# 하는데, 번을 초과하여 부상을 당하면 죽는다. 출구까지 죽지 않고 갈 수 있는지 검사하여 Yes 혹은 No를 출
# 력하는 프로그램을 순환함수(recursion)를 이용하여 작성하라.

# 입력 형식
# 표준입력파일(키보드)로 부터 입력을 받는다. 입력의 첫 줄에는 미로의 크기 이 주어진다. 이어진 줄에는 각 줄
# 마다 개의 0, 1, 혹은 2가 한 칸씩 띄어져서 주어진다. 0은 통로, 1은 지나갈 수 없는 벽, 그리고 2는 폭탄을 표시
# 한다. 마지막 줄에는 정수 의 값이 주어진다.
# 출력 형식
# Yes 혹은 No라고 출력한다.


# 0 == 통로
# 1 == 벽
# 2 == 폭탄
# 3 == 방문한적있는곳
# 4 == 방문했고 출구까지의 경로상에 있지않음


n = int(input())

maplist = []
for _ in range(n):
    maplist.append(list(map(int, input().split())))

k = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def findPath(x,y):
    if(x < 0 or x >= n or y < 0 or y >= n or maplist[x][y] != 0):
        return False
    elif(x == n-1 and y == n-1):
        maplist[x][y] = 3
        return True
    else:
        maplist[x][y] = 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if findPath(nx,ny):
                return True
        maplist[x][y] = 2
        return False
    
findPath(0,0)
if(maplist[n-1][n-1] == 3):
    print('yes')
else:
    print('no')

