
# 201812177 이문현

class Node:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.visited = False

    def check(self):
        self.visited = True
        return 1
    



class head:
    #using linklist's headL
    def __init__(self, word):
        self.word = word
        self.next = None
        self.end = None
        self.visited = False
        self.depth = -1
    
    def check(self):
        self.visited = True
        return 1
    
    def setDepth(self, level):
        self.depth = level

        
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


        
from collections import deque
def BFS(v: head, nDict : dict): 
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
            try:
                temp.check()
            except:
                return
            nodeWord = nDict[temp.word]
            if nodeWord.visited == False:
                nodeWord.check()
                nodeCount+=1
                queue.append(nodeWord.next)
            if temp.next == None:
                break
            temp=temp.next
    return nodeCount


nodeDict = {}
nodeDict_R = {}


n = int(input())
for i in range(n):
    p = head(i)
    q = head(i)
    nodeDict[i]=p
    nodeDict_R[i] = q

for _ in range(n):
    tmp = list(map(int,(input().split())))
    for i in range(tmp[1]):
        nodeDict[tmp[0]].addWord(tmp[i+2])
        nodeDict_R[tmp[i+2]].addWord(tmp[0])

# print("0의 연결노드")
# nodeDict[0].printLinkedList()
# print("1의 역방향 연결노드")
# nodeDict_R[3].printLinkedList()

# nodeDict_R[0].printLinkedList()
bfs1=BFS(nodeDict[0],nodeDict)
bfs2=BFS(nodeDict_R[0],nodeDict_R)
if bfs1 == bfs2 and bfs2 == n:
    print("YES")
else:
    print("NO")

    

# 5
# 0 2 2 3
# 1 4 0 2 3 4
# 2 1 4
# 3 0
# 4 1 3

# NO

# 5 0 2 2 3
# 1 3 0 2 4
# 2 1 4
# 3 1 1
# 4 1 3

# YES