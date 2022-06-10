
# 201812177 이문현

# 입력 = 사전파일
# 문장구조 = 단어\t설명





# 출력 (결과 3~4분 이내에 나오도록!)
# 문제
# 1. 그래프의 정점의 개수와 에지의 개수 출력
#     완성 후 전체 그래프를 돌면서 에지 카운트//2(무방향 그래프)
# 2. 최대 차수를 가지는 정점을 찾고 단어와 차수 출력
#     가장 깊은 연결리스트를 찾는다
# 3. 가장 큰 연결요소를 찾고, 연결요소의 크기를 출력(BFS로 각 연결요소 탐색)
# 4. 하나의 단어 x와 탐색깊이k 를 입력받고 단어 x로부터 떨어진 거리가 k 이하인 모든 단어를 찾아 한줄에 하나씩 출력한다.
#     이때 단어 x 자체를 맨 처음 출력하고, 나머지 단어들의 출력 순서는 마음대로 한다.
#         BFS, 큐의 형태를 이용해서(level order 방식) 해결 가능!
    

class Node:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.visited = False

    def check(self):
        self.visited = True
        return 1



class wordConnetction:
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
        print(self.word)
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

        
from collections import deque
def BFS(v: wordConnetction): 
    if v.visited:
        return 0
    # v를 이미 방문한 곳으로 처리 
    v.check()
    # 큐 선언 ,v를 큐에 추가해준다 
    nodeCount = 0
    queue = deque()
    queue.append(v)
    nodeCount += 1
    temp : wordConnetction 
    nodeWord : wordConnetction
    while queue:
        temp = queue.popleft()
        while(1):
            temp.check()
            nodeWord = wordDict[temp.word]
            if nodeWord.visited == False:
                nodeWord.check()
                nodeCount+=1
                queue.append(nodeWord.next)
            if temp.next == None:
                break
            temp=temp.next
    return nodeCount

def findDepth(word, k):
    start = []
    level = 0
    wordDict[word].setDepth(level)
    start.append(wordDict[word])
    queue = deque()
    queue.append(start)

    temp : wordConnetction
    nodeWord : wordConnetction
    
    while(level <= k):
        nodelist = queue.popleft()
        templist = []
        for t in nodelist:
            temp = t
            print(temp.word)
            # print(temp.word, level) #출력은 level 순으로 출력한다.
            while(1):
                nodeWord = wordDict[temp.word]
                if nodeWord.depth == -1:
                    nodeWord.setDepth(level+1)
                    templist.append(nodeWord)
                if temp.next == None:
                    break
                temp = temp.next

        if templist:
            queue.append(templist)
        level+=1


# 입력, 단어목록 생성 후 그래프 생성
# 1. 딕셔너리 생성{각 단어리스트의 헤드 주소 보관}
# 2. 문장에서 단어 읽고 노드 생성, 딕셔너리에 삽입 (단어:next노드(초기값 null))
# 3. 2번문장 eof까지 반복
# ->단어 목록 생성됨
wordDict = {} #각 단어 리스트의 head 주소를 보관

import os
path = os.path.dirname(os.path.abspath(__file__))+r'\dict_simplified.txt' #실행파일과 같은 폴더 내 dict_simplified.txt 경로 지정
# path = r"\dict_simplified.txt"                                             #또는 직접지정
count = 0
with open(path, 'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line or line == '\n':
            break
        line = line.split('\t',1)
        w = str(line[0])
        temp = wordConnetction(w)
        wordDict[w] = temp
        count+=1



#    그래프 제작
#   다시 파일의 설명부분을 읽어 각 단어가 dict 에 있는지 확인한다
#   단어 A 의 설명부분을 split 해 단어들의 리스트로 만든다
#   각 단어 B별 함수실행
#       문장별 dict에서 단어B를 찾는다. 만약 존재하면 A에 B를 추가하고 B에 A를 추가한다(중복시(이미 연결리스트에 있으면) 생략)
with open(path, 'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line or line == '\n':
            break
        line = line.split('\t',1)
        word = str(line[0])
        expl = line[1].split()
        for w in expl:
            if w in wordDict:
                wordDict[word].addWord(w)
                wordDict[w].addWord(word)
# print('graph made fin!')

edgeCount = 0
maxEdge = 0
maxWord = ""
for key in wordDict:
    temp = wordDict[key].countDepth()
    if temp > maxEdge:
        maxEdge = temp
        maxWord = key
    edgeCount+= temp
edgeCount = edgeCount//2
print("Answer1:",count ,edgeCount) 
print("Answer2:", maxWord, maxEdge)


# 연결 요소 BFS로 구하기
#   BFS함수로 각 연결요소들의 크기를 구한 뒤 max값을 구한다.

maxConnectComp = 0
for key ,value in wordDict.items():
    connectComp = BFS(value)
    if connectComp != 0:
        if maxConnectComp < connectComp:
            maxConnectComp = connectComp

print("Answer3:", maxConnectComp)
print("Answer4:",end=" ") 
w, k = input().split() #ex) mountain 2
findDepth(w, int(k))

os.system("pause")