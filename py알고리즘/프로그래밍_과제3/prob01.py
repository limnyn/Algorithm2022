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
    



class wordConnetction:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.end = None
        

    def addWord(self, linkword):
        newword = wordConnetction(linkword)
        if self.next == None:
            self.end = newword
            self.next = newword

        else:
            p = self.end
            p.next = newword
            self.end = newword
        
    def travel(self):
        print(self.word)
        p = self.next
        while(1):
            print(p.word)
            if (p.next == None):
                break
            else:
                p = p.next


        

# words = ['Apple', 'Banana', 'Choco']
# dict = wordConnetction(words[0])
# dict.addWord(words[1])
# dict.addWord(words[2])
# print(dict.word)
# dict.travel()
# line = 'aam	a dutch and german measure of liquids varying in different cities being at amsterdam about  wine gallons at antwerp   at hamburg'
# line = line.split('\t',1) # line[0] == 단어 line[1] == 뜻
# print(line)




# 연결리스트에 필요한 함수
# 1. 생성, 추가, [출력], 검색함수?
wordDict = {}
path = r"py알고리즘\프로그래밍_과제3\dict_simplified.txt"

count = 0

#입력
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


#출력
for key in wordDict:
    print(key,'=' ,wordDict[key].word)

print(count)
# 1. 딕셔너리 생성
    # 문장 받고 앞 단어만 읽기
        # line = line.split('\t',1) 로 해결
        # 라인 읽고 삽입해서 dict 생성하기
# 2. 문장에서 단어 읽고 노드 생성, 딕셔너리에 삽입 (단어:next노드(초기값 null))
# 3. 2번문장 eof까지 반복
# ->단어 목록 생성됨




