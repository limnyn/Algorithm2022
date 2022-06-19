


grid = []
grid.append([1,0,0,0,0,0,0,1])
grid.append([0,1,1,0,0,1,0,0])
grid.append([1,1,0,0,1,0,1,0])
grid.append([0,0,0,0,0,1,0,0])
grid.append([0,1,0,1,0,1,0,0])
grid.append([0,1,0,1,0,1,0,0])
grid.append([1,0,0,0,1,0,0,1])
grid.append([0,1,1,0,0,1,1,1])

WALL = 0
ROAD = 1
ALREADY_VISITED = 2
for g in grid:
    print(g)

def blobs(x, y):
    if(x < 0 or x > 7 or y< 0 or y > 7):
        return 0
    elif(grid[x][y] == WALL or grid[x][y] == ALREADY_VISITED):
        return 0
    else:
        grid[x][y] = ALREADY_VISITED
        return 1 + blobs(x+1,y) + blobs(x+1,y+1) + blobs(x,y+1) + blobs(x-1,y+1) + blobs(x-1,y) + blobs(x-1,y-1) + blobs(x,y-1) + blobs(x+1,y-1) 


countlist = []
for y in range(8):
    for x in range(8):
        temp = blobs(x,y)
        if(temp != 0):
            countlist.append(temp)

print(countlist)