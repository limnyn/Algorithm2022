# 3. 아래의 그림과 같은 N x N 크기의 2차원 미로가 입력으로 주어진다. 
# 출발점은 (0,0) 이고 도착점은 (N-1, N-1)이다. 
# 브레이크가 없는 자동차로 이동한다. 
# 브레이크가 없으므로 일단 한 방향으로 출발하면 장애물이나 외벽을 만나기 전에는 정지할 수 없고, 정지한 상태에서만 방향을 바꿀 수 있다.
# 예를 들어 아래 그림에서 초록 선과 같이 이동할 수는 없다. 하지만 붉은 선으로 표시된 경로를 따라 도착점까지 도달할 수는 있다.
# 출발점에서 도착점까지 이동할 수 있는지 검사하여 정지 횟수가 최소가 되는 경로를 찾아 출력하는 프로그램을 작성하라. 
# 경로가 존재하지 않으면 “No path”라고 출력한다.




# 0 == 통로
# 1 == 벽
# 2 == 폭탄
# 3 == 방문한적있는곳
# 4 == 방문했고 출구까지의 경로상에 있지않음

# n = int(input())
# maplist = []
# for _ in range(n):
#     maplist.append(list(map(int, input().split())))
# k = int(input())


# N=4
# maze=[[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,1,0,0]]

# N = 5
# maze = [[0,0,0,0,0],
#         [0,1,0,1,0],
#         [0,0,1,0,0],
#         [0,0,0,0,1],
#         [1,0,1,0,0]]
# N = 3
# maze = [[0,0,1],
#         [0,0,0],
#         [0,1,0]]
# N=8
# maze = [[0,0,1,0,0,0,0,0],
#         [0,0,1,1,1,0,0,0],
#         [0,0,0,0,1,0,1,0],
#         [0,0,0,0,1,0,0,1],
#         [0,1,1,0,1,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,1,0,0,0,1,0,0],
#         [0,0,1,1,1,0,0,0]]

N = int(input())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().split())))
dx = [1,0,-1,0]
dy = [0,1,0,-1]


stoplist =  []


def DFS(x, y,len,d):
    if x==N-1 and y==N-1:
        stoplist.append(len+1)

    else:
        nx = x+dx[d]    #진행방향의 다음 칸의 좌표
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N and maze[ny][nx]==0:
            xx=nx
            yy=ny
            maze[yy][xx]=1
            DFS(xx, yy,len,d)
            maze[yy][xx]=0
        # 조건세분화 필요, 벽일때 
        elif nx < 0 or ny < 0 or ny >= N or nx >= N or maze[ny][nx] == 1:
            for i in range(2):
                d = (d + i + 1)%4
                xx=x+dx[d]
                yy=y+dy[d]
                if 0<=xx<N and 0<=yy<N and maze[yy][xx]==0:
                    maze[yy][xx]=1
                    DFS(xx, yy,len+1,d)
                    maze[yy][xx]=0
                else:
                    continue


DFS(0,0,0,0)
DFS(0,0,0,1)
    
if(len(stoplist)==0):
    print('No path')
else:
    print(min(stoplist))





# ###
# N = 3
# maze = [[0,0,1],
#         [0,0,0],
#         [0,1,0]]
        
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]


# stoplist =  []

# cnt = 0

# def DFS(x, y,len):
#     global cnt
#     if x==N-1 and y==N-1:
#         stoplist.append(len)
#         cnt+=1

#     else:
#         for i in range(4):
#             xx=x+dx[i]
#             yy=y+dy[i]
#             if 0<=xx<N and 0<=yy<N and maze[yy][xx]==0:
#                 maze[yy][xx]=1
#                 DFS(xx, yy,len+1)
#                 maze[yy][xx]=0

                
# DFS(0,0,0)
# print(cnt)
    
    
# print(stoplist)

