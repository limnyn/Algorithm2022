colums = [0,0,0,0]

def nqueens(lv):
    if colums[lv-1] - colums[lv] == -1 or colums[lv-1] - colums[lv] == 1:
        return False
    elif lv == 3:
        return True
    else:
        for i in range(4):
            if(i+1 in colums):
                continue
            else:
                colums[lv+1] = i+1
                if nqueens(lv+1):
                    print(colums)

for i in range(4):
    colums[0] = i + 1
    if nqueens(0):
        break

