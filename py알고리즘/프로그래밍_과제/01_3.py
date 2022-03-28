# 3. 아래의 그림과 같은 N x N 크기의 2차원 미로가 입력으로 주어진다. 
# 출발점은 (0,0) 이고 도착점은 (N-1, N-1)이다. 
# 브레이크가 없는 자동차로 이동한다. 
# 브레이크가 없으므로 일단 한 방향으로 출발하면 장애물이나 외벽을 만나기 전에는 정지할 수 없고, 정지한 상태에서만 방향을 바꿀 수 있다.
# 예를 들어 아래 그림에서 초록 선과 같이 이동할 수는 없다. 하지만 붉은 선으로 표시된 경로를 따라 도착점까지 도달할 수는 있다.
# 출발점에서 도착점까지 이동할 수 있는지 검사하여 정지 횟수가 최소가 되는 경로를 찾아 출력하는 프로그램을 작성하라. 
# 경로가 존재하지 않으면 “No path”라고 출력한다.


n = int(input())

maplist = []
for _ in range(n):
    maplist.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque

for i in range(n):
    for j in range(n):
        if maplist[i][j] == 1:
            maplist[i][j] = 0
        elif maplist[i][j] == 0:
            maplist[i][j] = 1
    
def bfs(x,y):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 벽인 경우 무시
            if maplist[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maplist[nx][ny] == 1:
                maplist[nx][ny] = maplist[x][y] + 1
                queue.append((nx,ny))
            # 가장 오른쪽 아래까지의 최단 거리 반환
    return maplist[n-1][n-1]

print(bfs(0,0))


