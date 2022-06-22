import sys
sys.setrecursionlimit(10**7)
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
        self.color = 0

    def check(self):
        self.visited = True
        return 1
    
    def setDepth(self, level):
        self.depth = level

        
    def addNode(self, linkword):
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
        
    def printLinkedList(self): #print until end
        print(self.word, ':', end=" ")
        p = self.next
        while(1):
            print(p.word, end=" ")
            if (p.next == None):
                print()
                break
            else:
                p = p.next

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

from collections import deque
import os
path = os.path.dirname(os.path.abspath(__file__))+r'\inputRB.txt' #실행파일과 같은 폴더 내 input.txt 경로 지정
sumlist = []
indexlist = []#연결요소 시작 노드를 가리킴, 시작노드는 -1값 가짐
headlist = {}

with open(path, 'r',encoding='utf-8') as f:
    firstLine = f.readline().split()
    nodeCount=int(firstLine[0])
    edgeCount=int(firstLine[1])
    for i in range(nodeCount):

        headlist[i]=head(i)


    for _ in range(edgeCount):
        line = f.readline()
        line = line.split()
        line = list(map(int, line))
        startNode = line[0]
        endNode= line[1]
        tmp : head
        tmp = headlist[startNode]
        tmp.addNode(endNode)
        tmp = headlist[endNode]
        tmp.addNode(startNode)

# for i in range(nodeCount):
#     print(headlist[i].countDepth())




# 젤 처음 0번노드 칠하고
# 주변노드 색 다 칠하기


# 그냥 for문해서 딕셔너리로
# 각 간선별로 색을 검사한다
#     1. 비어있다
#         다른색 색칠
#     2. 칠해져있다
#         다른색 색
#             컨티뉴
#         같은색
#             프린트 후 브레이크
color = 1
headlist[0].color=color
end = 0
for i in range(nodeCount):
    n = headlist[i]
    nodePerEdge = n.countDepth()
    nodeColor = n.color
    p = n
    # 만약 색이없으면 엣지에 색 있는게 존재하는지 검사!
    if nodeColor == 0:
        for _ in range(nodePerEdge):
            p=p.next
            nextcolor = headlist[p.word].color 
            if nextcolor == 0:
                continue
            elif nextcolor != 0:
                headlist[i].color = (-1)*nextcolor
                break

    p = n
    for _ in range(nodePerEdge):
        p=p.next
        nextcolor = headlist[p.word].color 
        if nextcolor == 0:
            headlist[p.word].color = color*(-1)
        elif nextcolor == nodeColor:
            print("No")
            end=1
            break
        elif nextcolor == nodeColor*(-1):
            continue
            
    if end == 1:
        break
if end == 0:
    print("Yes")

# 결과적으로 for문 반복횟수는 O(2m)을 넘지않는다.