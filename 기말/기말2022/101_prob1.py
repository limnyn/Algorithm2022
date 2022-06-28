
# import os
# path = os.path.dirname(os.path.abspath(__file__))+r'\input2.txt' #실행파일과 같은 폴더 내 input.txt 경로 지정



class Node:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.visited = False

    def check(self):
        self.visited = True
        return 1



class head:
    #using linklist's head
    def __init__(self, word):
        self.word = word
        self.next = None
        self.end = None
        self.visited = False
        self.depth = -1
    
    def check(self):
        self.visited = True
        return 1
    
    # def setDepth(self, level):
    #     self.depth = level

        
    def addWord(self, linkword):
        if self.find(linkword)==True: # if is already in linked list, skip
            return False
        newword = Node(linkword)
        if self.next == None:
            self.end = newword
            self.next = newword
        else:
            p = self.end
            p.next = newword
            self.end = newword
        return True
        
    # def printLinkedList(self): #print until end
    #     print(self.word)
    #     p = self.next
    #     while(1):
    #         print(p.word)
    #         if (p.next == None):
    #             break
    #         else:
    #             p = p.next

    def find(self, target): # mean is in linklist? return t/f
        if self.word == target:
            return True
        p = self.next
        while(1):
            if p == None:
                return False
            if (p.word == target):
                return True
            if (p.next == None):
                return False
            else:
                p = p.next

    # def countDepth(self): # return node's edges
    #     depthCount = 0
    #     if self.next == None:
    #         return 0
    #     p = self.next
    #     while(1):
    #         if (p.next == None):
    #             depthCount+=1
    #             return depthCount
    #         else:
    #             depthCount+=1
    #             p = p.next

nodeDict = {}

        
from collections import deque
def BFS(v: head): 
    if v.visited:
        return 0
    # v를 이미 방문한 곳으로 처리 
    v.check()
    # 큐 선언 ,v를 큐에 추가해준다 
    nodeCount = 0
    queue = deque()
    queue.append(v)
    nodeCount += 1
    temp : head 
    nodeWord : head
    while queue:
        temp = queue.popleft()
        while(1):
            temp.check()
            nodeWord = nodeDict[temp.word]
            if nodeWord.visited == False:
                nodeWord.check()
                nodeCount+=1
                queue.append(nodeWord.next)
            if temp.next == None:
                break
            temp=temp.next
    return nodeCount

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
    h = head(i)
    for j in range(n):
        if nodeGraph[i][j] == 1:
            h.addWord(j)
            nodelist[i].append(j)
    nodeDict[i] = h



maxConnectComp = []
for key ,value in nodeDict.items():
    connectComp = BFS(value)
    if connectComp != 0:
            print(connectComp, end= " ")

print()


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