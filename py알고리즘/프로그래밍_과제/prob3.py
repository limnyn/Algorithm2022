# 3. 아래의 그림과 같은 N x N 크기의 2차원 미로가 입력으로 주어진다. 
# 출발점은 (0,0) 이고 도착점은 (N-1, N-1)이다. 
# 브레이크가 없는 자동차로 이동한다. 
# 브레이크가 없으므로 일단 한 방향으로 출발하면 장애물이나 외벽을 만나기 전에는 정지할 수 없고, 정지한 상태에서만 방향을 바꿀 수 있다.
# 예를 들어 아래 그림에서 초록 선과 같이 이동할 수는 없다. 하지만 붉은 선으로 표시된 경로를 따라 도착점까지 도달할 수는 있다.
# 출발점에서 도착점까지 이동할 수 있는지 검사하여 정지 횟수가 최소가 되는 경로를 찾아 출력하는 프로그램을 작성하라. 
# 경로가 존재하지 않으면 “No path”라고 출력한다.



# 입력에#########################################

# N=4
# maze=[[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,1,0,0]]
##출력 = No path


# N = 5
# maze = [[0,0,0,0,0],
#         [0,1,0,1,0],
#         [0,0,1,0,0],
#         [0,0,0,0,1],
#         [1,0,1,0,0]]
##출력 = 4


# N = 3
# maze = [[0,0,1],
#         [0,0,0],
#         [0,1,0]]
##출력 = 4


# N=8
# maze = [[0,0,1,0,0,0,0,0],
#         [0,0,1,1,1,0,0,0],
#         [0,0,0,0,1,0,1,0],
#         [0,0,0,0,1,0,0,1],
#         [0,1,1,0,1,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,1,0,0,0,1,0,0],
#         [0,0,1,1,1,0,0,0]]
# #출력 = 8





#입력부분#######
n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))


#방향
dx = [1,0,-1,0]
dy = [0,1,0,-1]
stoplist =  []      #도착시 정지횟수 기록



def DFS(x, y,stopCount,d):
    if x==n-1 and y==n-1:
        stoplist.append(stopCount+1)    #도착점도 포함해서 카운트

    else:
        nx = x+dx[d]    #진행방향의 다음 칸의 좌표 nextX nextY
        ny = y+dy[d]
        if 0<=nx<n and 0<=ny<n and maze[ny][nx]==0: #다음칸이 벽과 테두리가 아닐때
            xx=nx
            yy=ny
            maze[yy][xx]=1
            DFS(xx, yy,stopCount,d)                 #진행방향 유지후 재귀
            maze[yy][xx]=0
        elif nx < 0 or ny < 0 or ny >= n or nx >= n or maze[ny][nx] == 1:
            for i in range(2):
                d = (d + i + 1)%4                   # 충돌시 가로축진행->세로축 진행, 세로축진행-> 가로축진행으로 방향전환
                xx=x+dx[d]
                yy=y+dy[d]
                if 0<=xx<n and 0<=yy<n and maze[yy][xx]==0:
                    maze[yy][xx]=1
                    DFS(xx, yy,stopCount+1,d)       #진행방향 변환, 정지횟수 +1후 재귀
                    maze[yy][xx]=0
                else:
                    continue


#미로시작시 테두리를 제외한 오른쪽, 아래쪽 방향으로만 시작
DFS(0,0,0,0)
DFS(0,0,0,1)
    
if(len(stoplist)==0):       #목적지 도달한 기록이 없을때
    print('No path')
else:                       #목적지 도달 시 최소 정지횟수 출력
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

# def DFS(x, y,stopCount):
#     global cnt
#     if x==N-1 and y==N-1:
#         stoplist.append(stopCount)
#         cnt+=1

#     else:
#         for i in range(4):
#             xx=x+dx[i]
#             yy=y+dy[i]
#             if 0<=xx<N and 0<=yy<N and maze[yy][xx]==0:
#                 maze[yy][xx]=1
#                 DFS(xx, yy,stopCount+1)
#                 maze[yy][xx]=0

                
# DFS(0,0,0)
# print(cnt)
    
    
# print(stoplist)

