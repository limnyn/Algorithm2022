
# import os
# path = os.path.dirname(os.path.abspath(__file__))+r'\input2.txt' #실행파일과 같은 폴더 내 input.txt 경로 지정


sumlist = []
indexlist = []#연결요소 시작 노드를 가리킴, 시작노드는 -1값 가짐




n = int(input())
nodeGraph = []
nodelist = []
sum = [] 

for _ in range(n):
    nodeGraph.append(list(map(int, (input().split()))))

    nodelist.append([])

for i in range(n):
    for j in range(i,n):
        if nodeGraph[i][j] == 1:
            nodelist[i].append(j)




for _ in range(n):
    sumlist.append(0)
    sum.append(0) 

    indexlist.append(-1)
for i in range(n):
        # if len(nodelist[i]) == 0:
        #     continue
     for j in range(len(nodelist[i])):
            
    # for _ in range(edgeCount):
        startNum = i
        endNum = nodelist[i][j]
        if sumlist[startNum] >= 0:
            sumlist[endNum]= -1
            tmp = startNum
            q=-9999
            while(1):
                if tmp != -1:
                    q = tmp
                    tmp =indexlist[q]
                else:
                    break

            indexlist[endNum]=  q
            # sumlist[q] += 1
                
        elif sumlist[startNum] == -1:
            sumlist[endNum]= -1
            q = startNum
            p = indexlist[startNum]
                
            if indexlist[startNum] != -1:
                    
                while(1):
                    if p == -1:
                        break
                    q = p
                    p = indexlist[q]

                    
            indexlist[endNum] = q
            # sumlist[q] += 1



result = []
for item in indexlist:
    if item != -1:
        sum[item]+=1
for item in sum:
    if item != 0:
        print(item+1, end=" ")

print()


# print(indexlist)

# 9
# 0 1 0 1 0 0 0 0 0
# 1 0 1 1 0 0 0 0 0
# 0 1 0 1 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0
# 0 0 0 0 1 0 1 0 0
# 0 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 1 0

# 11

# 0 0 0 1 0 0 0 1 0 0 1
# 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 1 0 0 0 0 0 0 0
# 1 0 1 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 1
# 0 0 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0 0
# 0 0 0 1 0 1 0 0 0 0 1
# 1 0 0 0 0 1 0 0 0 1 0
