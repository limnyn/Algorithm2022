
class Node:
    def __init__(self, name, distance):
        self.name = int(name)
        self.distance = int(distance)
        self.next = None
        self.visited = False

    def check(self):
        self.visited = True
        return 1

        
    def add(self, target):
        if self.find(target)==True: # if is already in linked list, skip
            return False
        newNode = Node(target.name, target.distance)
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
        
    def weightSum(self): #print until end
        sum = self.distance
        p = self.next
        while(1):
            if (p == None):
                break            
            
            sum += p.distance
            p = p.next
        return sum






graph = {} 

import os
path = os.path.dirname(os.path.abspath(__file__))+r'\input2.txt' #실행파일과 같은 폴더 내 input.txt 경로 지정
count = 0
nodelist = []
with open(path, 'r',encoding='utf-8') as f:
    firstLine = f.readline().split()
    nodeCount=int(firstLine[0])
    edgeCount=int(firstLine[1])
    for i in range(nodeCount):
        graph[i] = Node(i,0)
    while True:
        line = f.readline()
        if not line or line == '\n':
            break
        line = line.split()
        
   
        tmp = graph[int(line[0])] 
        adder = Node(line[1],line[2])
        tmp.add(adder)
        tmp2 = graph[int(line[1])] 
        adder2 = Node(line[0],line[2])
        tmp2.add(adder)

        count+=1


for w in range(nodeCount):
    t = graph[w]
    print(w, t.name, t.distance)
print('print graph')



from collections import deque
def BFS(v: Node): 
    compList=[]
    if v.visited:
        return compList
    compList.append(v)
    # v를 이미 방문한 곳으로 처리 
    v.check()
    # 큐 선언 ,v를 큐에 추가해준다 
    # nodeC = 0
    queue = deque()
    queue.append(v)
    # nodeC += 1
    temp : Node 
    nodeWord : Node
    while queue:
        temp = queue.popleft()
        while(1):
            if temp == None:
                break
            temp.check()
            nodeWord = graph[temp.name]
            if nodeWord.visited == False:
                nodeWord.check()
                compList.append(nodeWord)
                # nodeC+=1
                queue.append(nodeWord.next)
            if temp.next == None:
                break
            temp=temp.next
    return compList


maxConnectComp = 0
maxSum = -1

for key ,value in graph.items():
    compList = BFS(value)
    # print(len(compList))
    result = 0
    for n in compList:
        n:Node
        result += n.weightSum()
    # result = result //2
    print(result)
    if result > maxSum:
        maxSum = result
  
print("연결요소간 노드 가중치합중 최대값:", maxSum)


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



    