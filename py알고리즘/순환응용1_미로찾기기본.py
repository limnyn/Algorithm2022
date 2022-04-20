# 다음은 출발점(0,0)으로부터 출구 (N-1, N-1)까지 도달하는 가장 긴 경로의 길이를 구하여 반환하는 함수이다.
# 경로가 존재하지 않으면 -1을 반환한다.
# 미로에서 통로는 0, 벽은 1이라고 가정한다.
# 맨 처음 이 함수는 MazePath(0,0,0)으로 호출된다. 완성하라.


N = 3
maze = [[0,1,1],
        [0,1,1],
        [0,0,0]]
        
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def mazePath(x,y):
    if(x<0 or y<0 or x>= N or y>=N or maze[x][y] != 0):
        return False
    elif (x == N-1 and y == N-1):
        return True
    else:
        maze[x][y]=2
        for i in range(4):
            if(mazePath):
                return True

        return False

    
    
print(mazePath(0,0))

