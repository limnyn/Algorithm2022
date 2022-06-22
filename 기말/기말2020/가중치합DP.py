
import os
path = os.path.dirname(os.path.abspath(__file__))+r'\input2.txt' #실행파일과 같은 폴더 내 input.txt 경로 지정
sumlist = []
indexlist = []#연결요소 시작 노드를 가리킴, 시작노드는 -1값 가짐

with open(path, 'r',encoding='utf-8') as f:
    firstLine = f.readline().split()
    nodeCount=int(firstLine[0])
    edgeCount=int(firstLine[1])
    for _ in range(nodeCount):
        sumlist.append(0)
        indexlist.append(-1)

    for _ in range(edgeCount):
        line = f.readline()
        line = line.split()
        line = list(map(int, line))
        startNum = line[0]
        endNum = line[1]
        weight = line[2]


        if sumlist[startNum] >= 0:
            sumlist[endNum]= -1
            indexlist[endNum]= startNum
            sumlist[startNum] += weight
            
            # index = startNum
        elif sumlist[startNum] == -1:
            sumlist[endNum]= -1
            sumlist[indexlist[startNum]] += weight

        
print(max(sumlist))
print(sumlist)
print(indexlist)

# 0   1   2   3   4   5   6   7   8
# 11 -1  -1  -1   12 -1  -1   6  -1
# -1  0   0   0  -1   4   4  -1   7