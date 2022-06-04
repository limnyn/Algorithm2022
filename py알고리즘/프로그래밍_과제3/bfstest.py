# 입력 = 사전파일
# 구조 = 단어\t설명

# 1. 딕셔너리 생성
# 2. 문장에서 단어 읽고 노드 생성, 딕셔너리에 삽입 (단어:next노드(초기값 null))
# 3. 2번문장 eof까지 반복
# ->단어 목록 생성됨


# 출력 (결과 3~4분 이내에 나오도록!)
# 1. 그래프의 정점의 개수와 에지의 개수 출력
#     완성 후 전체 그래프를 돌면서 에지 카운트//2(무방향 그래프?)
# 2. 최대 차수를 가지는 정점을 찾고 단어와 차수 출력
#     가장 깊은 연결리스트를 찾는다
# 3. 가장 큰 연결요소를 찾고, 연결요소의 크기를 출력(BFS나 DFS로 각 연결요소 탐색)
#     https://velog.io/@kjh107704/%EA%B7%B8%EB%9E%98%ED%94%84-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C
# 4. 하나의 단어 x와 탐색깊이k 를 입력받고 단어 x로부터 떨어진 거리가 k 이하인 모든 단어를 찾아 한줄에 하나씩 출력한다.
#     이때 단어 x 자체를 맨 처음 출력하고, 나머지 단어들의 출력 순서는 마음대로 한다.
#         BFS, 큐의 형태를 이용해서(level order 방식) 해결 가능!
    
import time


class wordConnetction:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.end = None
        self.visited = False
        self.depth = -1
    
    def check(self):
        self.visited = True
        return 1

        
    def addWord(self, linkword):
        if self.find(linkword)==True: # if is already in linked list, skip
            return False
        newword = wordConnetction(linkword)
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
    
    
        



# 1. 딕셔너리 생성
    # 문장 받고 앞 단어만 읽기
        # line = line.split('\t',1) 로 해결
        # 라인 읽고 삽입해서 dict 생성하기

#입력
wordDict = {}
path = r"py알고리즘\프로그래밍_과제3\bfstest.txt"

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

# #단어와 갯수 출력
# for key in wordDict:
#     print(key,'=' ,wordDict[key].word)
# print(count)


# 2. 그래프 제작
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
        print(expl)
        for w in expl:
            if w in wordDict:
                wordDict[word].addWord(w)
                wordDict[w].addWord(word)

print('graph made fin!')
# wordDict['mountain'].travel()
# print(wordDict['mountain'].countDepth())


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
print("노드의 개수 : ",count,"에지의 개수 : ",edgeCount) # 에지의 개수 정답 확인필요, 테스트결과는 이상 X 
print("최대 차수를 가지는 정점의 단어 : ", maxWord, "차수 : ", maxEdge)


# 연결 요소 BFS로 구하기
#   BFS함수로 각 연결요소를 구하고 크기를 구한 뒤 max값을 구한다.
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
        # for _ in range(temp.countDepth):
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



time0 = time.time()
# beta = wordDict["beta"]
# beta.check()
# print(beta.visited)
# maxConnectComp = BFS(wordDict["beta"])
maxConnectComp = 0
for key ,value in wordDict.items():
    connectComp = BFS(value)
    if connectComp != 0:
        if maxConnectComp < connectComp:
            maxConnectComp = connectComp


print("가장 큰 연결요소 : ", maxConnectComp)
print("연결요소 수행시간 = ",time.time()-time0)





                    
#확인필요

    # while 큐가 비어있지 않다면:
    #     큐에서 v를 pop해준다 
    #     for v에 연결된 각각의 정점 i에 대하여:
    #         if i에 아직 방문하지 않았다면:
    #             i를 방문한 곳으로 처리한다 
    #             큐에 i를 추가한다

# #test parts
# words = ['Apple', 'Banana', 'Choco']
# dict = wordConnetction(words[0])
# dict.addWord(words[1])
# dict.addWord(words[2])

# print(dict.addWord('thaco'))

# dict.travel()
# print(dict.countDepth())
