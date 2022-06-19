# 1.섬문제
#   연결요소 최대크기 출력하는것
#   연결 여부는 반지름*2보다 거리가 좁을경우

# A B간의 거리계산함수
#     중심 사이 거리계산
#     그렇게 각 노드간 그래프 생성

#     이후 연결요소 리스트 만들어서 최대값 찾기


class Node:
    def __init__(self, name, posX,posY, rad):
        self.name = int(name)
        self.x = int(posX)
        self.y = int(posY)
        self.rad = int(rad)
        self.next = None
        self.visited = False

    def check(self):
        self.visited = True
        return 1

        
    def add(self, target):
        if self.find(target)==True: # if is already in linked list, skip
            return False
        newNode = Node(target.name, target.x,target.y,target.rad)
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


def isconnected(a, b):
    distsquare = (a.y-b.y)**2 + (a.x-b.x)**2
    if (2*(a.rad+b.rad))**2 >= distsquare:
        return True
    else:
        return False





graph = {} #각 단어 리스트의 head 주소를 보관

import os
path = os.path.dirname(os.path.abspath(__file__))+r'\input.txt' #실행파일과 같은 폴더 내 input.txt 경로 지정
# path = r"\dict_simplified.txt"                                             #또는 직접지정
count = 0
nodelist = []
with open(path, 'r',encoding='utf-8') as f:
    nodeCount = int(f.readline())

    while True:
        line = f.readline()
        if not line or line == '\n':
            break
        line = line.split()
        
        graph[count] = Node(str(count),line[0],line[1],line[2])
        count+=1


for w in range(count):
    t = graph[w]
    print(w, t.name, t.x, t.y, t.rad)
print('print graph')

for i in range(0,nodeCount):
    anode = graph[i]
    for j in range(0,nodeCount):
        bnode = graph[j]
        if isconnected(anode,bnode):
            anode.add(bnode)
            bnode.add(anode)

for w in range(count):
    t = graph[w]
    t.printLinkedList()


from collections import deque
def BFS(v: Node): 
    if v.visited:
        return 0
    # v를 이미 방문한 곳으로 처리 
    v.check()
    # 큐 선언 ,v를 큐에 추가해준다 
    nodeC = 0
    queue = deque()
    queue.append(v)
    nodeC += 1
    temp : Node 
    nodeWord : Node
    while queue:
        temp = queue.popleft()
        while(1):
            temp.check()
            nodeWord = graph[temp.name]
            if nodeWord.visited == False:
                nodeWord.check()
                nodeC+=1
                queue.append(nodeWord.next)
            if temp.next == None:
                break
            temp=temp.next
    return nodeC


maxConnectComp = 0
for key ,value in graph.items():
    connectComp = BFS(value)
    if connectComp != 0:
        if maxConnectComp < connectComp:
            maxConnectComp = connectComp

print("Answer3:", maxConnectComp)


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



    