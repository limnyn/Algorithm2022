# 1.연못문제

# A B간의 거리계산함수
#     변 사이에 꼭짓점 = 같은 좌표 공유, 다른 축거리
#     변 사이에 꼭짓점 안걸침 = 꼭짓점 간 거리 최소

#     그렇게 각 노드간 그래프 생성
#     bfs를 통해 최단경로 찾기
# 다 풀었지만 이거 문제가 있음 그래프 연결이 좀 이상함 사각형간 거리구하기 공식수정필요!


class Node:
    def __init__(self, name, a,b,w,h):
        self.name = int(name)
        self.A = int(a)
        self.B = int(b)
        self.W = int(w)
        self.H = int(h)
        self.next = None
        self.visited = False
        self.depth = -1


    def check(self):
        self.visited = True
        return 1

        
    def add(self, target):
        if self.find(target)==True: # if is already in linked list, skip
            return False
        newNode = Node(target.name, target.A,target.B,target.W,target.H)
        if self.next == None:
            self.end = newNode
            self.next = newNode
        else:
            p = self.end
            p.next = newNode
            self.end = newNode
        return True

    def find(self, target): # mean is in linklist? return t/f
        if self.name == target.name:
            return True
        p = self.next
        while(1):
            if p == None:
                return False
            if (p.name == target.name):
                return True
            if (p.next == None):
                return False
            else:
                p = p.next
    def printLinkedList(self): #print until end
        print(self.name,end=" ")
        p = self.next
        while(1):
            if p == None:
                break
            print(p.name,end=" ")
            if (p.next == None):
                break
            else:
                p = p.next
        print()

    
    def setDepth(self, level):
        self.depth = level

    def countDepth(self): # return node's edges
        depthCount = 0
        if self.next == None:
            return 0
        p = self.next
        while(1):
            if (p.next == None):
                depthCount+=1
                return depthCount
            else:
                depthCount+=1
                p = p.next


#연결되어있는지 확인
def isconnected(a, b, D):
    if (a.A <= b.A and a.A+a.W >= b.A) or (b.A <= a.A and b.A+b.W >= a.A) or (a.A <= b.A+b.W and a.A+a.W >= b.A+b.W) or (b.A <= a.A+a.W and b.A+b.W >= a.A+a.W):
        dist = min(abs(a.B+a.H - b.B+b.H), abs(a.B+a.H - b.B), abs(a.B - b.B+b.H), abs(a.B - b.B))
        dist = dist**2
    elif (a.B <= b.B and a.B+a.H >= b.B) or (b.B <= a.B and b.B+b.H >= a.B) or (a.B <= b.B+b.H and a.B+a.H >= b.B+b.H) or (b.B <= a.B+a.W and b.A+b.W >= a.B+a.W):
        dist = min(abs(a.A+a.W - b.A+b.W), abs(a.A+a.W - b.A), abs(a.A - b.A+b.W), abs(a.A - b.A))
        dist = dist**2
    else:
        spotA = [(a.A,a.B),(a.A+a.W,a.B),(a.A+a.W,a.B),(a.A+a.W,a.B+a.H)]
        spotB = [(b.A,b.B),(b.A+b.W,b.B),(b.A+b.W,b.B),(b.A+b.W,b.B+b.H)]
        distlist = []
        for i in range(len(spotA)):
            for j in range(len(spotB)):
                dist = (spotA[i][0]-spotB[i][0])**2 + (spotA[i][1]-spotB[i][1])**2
                distlist.append(dist)
        dist = min(distlist)
            
    
    if D >= dist:
        return True
    else:
        return False





graph = {} #각 단어 리스트의 head 주소를 보관

import os
path = os.path.dirname(os.path.abspath(__file__))+r'\input1.txt' #실행파일과 같은 폴더 내 input1.txt 경로 지정
# path = r"\dict_simplified.txt"                                             #또는 직접지정
count = 0
nodelist = []
with open(path, 'r',encoding='utf-8') as f:
    firstline = f.readline().split()
    nodeCount=int(firstline[0])
    limitDistance=int(firstline[1])
    
    while True:
        line = f.readline()
        if not line or line == '\n':
            break
        line = line.split()
        if len(line) == 2:
            start = int(line[0])
            end = int(line[1])
            break
        graph[count] = Node(str(count),line[0],line[1],line[2],line[3])
        count+=1


for i in range(0,nodeCount):
    anode = graph[i]
    for j in range(0,nodeCount):
        bnode = graph[j]
        if isconnected(anode,bnode,limitDistance):
            anode.add(bnode)
            bnode.add(anode)



from collections import deque

 
def findDepth(word, k,dest):
    start = []
    level = 0
    graph[word].setDepth(level)
    start.append(graph[word])
    queue = deque()
    queue.append(start)

    temp : Node
    nodeWord : Node
    
    while(level <= k):
        nodelist = queue.popleft()
        templist = []
        for t in nodelist:
            temp = t
            if temp.name == graph[dest].name:
                print(level)
                return level
            
            # print(temp.word, level) #출력은 level 순으로 출력한다.
            while(1):
                nodeWord = graph[temp.name]
                if nodeWord.depth == -1:
                    nodeWord.setDepth(level+1)
                    templist.append(nodeWord)
                if temp.next == None:
                    break
                temp = temp.next

        if templist:
            queue.append(templist)
        level+=1



try:
    findDepth(start, 9999, end)
except:
    print("No Path")


# #    그래프 제작
# #   다시 파일의 설명부분을 읽어 각 단어가 dict 에 있는지 확인한다
# #   단어 A 의 설명부분을 split 해 단어들의 리스트로 만든다
# #   각 단어 B별 함수실행
# #       문장별 dict에서 단어B를 찾는다. 만약 존재하면 A에 B를 추가하고 B에 A를 추가한다(중복시(이미 연결리스트에 있으면) 생략)
# with open(path, 'r',encoding='utf-8') as f:
#     while True:
#         line = f.readline()
#         if not line or line == '\n':
#             break
#         line = line.split('\t',1)
#         word = str(line[0])
#         expl = line[1].split()
#         for w in expl:
#             if w in graph:
#                 graph[word].addWord(w)
#                 graph[w].addWord(word)
# # print('graph made fin!')



   