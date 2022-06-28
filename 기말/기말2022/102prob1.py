
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
        
    def printLinkedList(self): #print until end
        # print(self.word)
        p = self.next
        while(1):
            print(p.word)
            if (p.next == None):
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
        
    def resetDepthVisit(self): #print until end
        self.depth = -1
        self.visited = False
        p = self.next
        p.depth = -1
        while(1):
            p.visited = False
            if (p.next == None):
                break
            else:
                p = p.next


        
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

def findDepth(word, k):
    for i in range(n):
        nodeDict[i].resetDepthVisit()
    count = 0
    start = []
    level = 0
    nodeDict[word].setDepth(level)
    start.append(nodeDict[word])
    queue = deque()
    queue.append(start)

    temp : head
    nodeWord : head
    
    while(level <= k):
        try:    nodelist = queue.popleft()
        except:
            break
        templist = []
        for t in nodelist:
            temp = t
            # print(temp.word)
            count+=1

            while(1):
                nodeWord = nodeDict[temp.word]
                if nodeWord.depth == -1:
                    nodeWord.setDepth(level+1)
                    templist.append(nodeWord)
                if temp.next == None:
                    break
                temp = temp.next

        if templist:
            queue.append(templist)
        level+=1
   
    return count





grapharr=[]
n = int(input())
for _ in range(n):
    grapharr.append(list(map(int,(input().split()))))

nodeDict = {}

for i in range(n):
    tmp = head(i)
    for j in range(n):
        if grapharr[i][j] == 1:
            tmp.addWord(j)
    nodeDict[i] = tmp






k = int(input()) #ex) mountain 2
maxnode = -1
maxcount = -1
# li = []
for i in range(n):
    result = findDepth(i, k)
    # li.append(result)
    if result >= maxcount :
        maxcount=result
        maxnode = i

# maxcount=findDepth(6,k)
print(maxnode, maxcount)
# print(6, maxcount)

# 9  
# 0 1 0 1 0 0 0 0 0
# 1 0 1 0 0 0 1 0 0
# 0 1 0 1 0 0 0 0 0
# 1 0 1 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 1
# 0 0 0 0 1 0 1 0 1
# 0 1 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 1
# 0 0 0 0 1 1 0 1 0
# 2



# 11
# 0 0 0 1 0 0 0 1 0 0 1
# 0 0 0 0 0 0 1 0 1 0 1
# 0 0 0 1 0 0 0 0 0 0 0
# 1 0 1 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 0 0
# 0 1 0 0 1 0 0 0 0 0 0     
# 0 0 0 1 0 1 0 0 0 0 1
# 1 1 0 0 0 1 1 0 0 1 0
# 2