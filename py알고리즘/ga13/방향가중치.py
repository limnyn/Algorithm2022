from ga13_2최단경로개수 import printSolution
from ga13_2최단경로개수 import floydWarshall
from ga13_2최단경로개수 import printPath


#입력->연결리스트로 그래프생성->그래프를 행렬로-> 행렬으로 최단경로 경우의수 출력하는 프로그램!
class eNode():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.next = None


class Node():
    def __init__(self, head):
        self.head = head
        self.next = None

    def addEdge(self, Edge, weight):
        if self.next == None:
            self.next = eNode(Edge,weight)
        else:
            p:eNode
            p = self.next
            while(1):
                if p.next == None:
                    p.next = eNode(Edge,weight)
                    break
                p = p.next

    def printEdge(self):
        print(self.head, end=" : ")
        p:eNode
        p = self.next
        while(1):
            if p == None:
                print()
                break
            print("[{}, {}]".format(p.name,p.weight), end=" ")
            p = p.next

    def edgeNum(self):
        num = 0
        if self.next == None:
            return num
        else:
            p:eNode
            p = self.next
            while(1):
                num+=1
                if p.next == None:
                    return num
                p = p.next

    

graph = []

a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)

a.addEdge(2, -2)
b.addEdge(0,4)
b.addEdge(2,3)
c.addEdge(3,2)
d.addEdge(1,-1)



graph.append(a)
graph.append(b)
graph.append(c)
graph.append(d)

for n in graph:
    n:Node
    n.printEdge()


edgeSum = 0
for i in graph:
    i:Node
    edgeSum += i.edgeNum()

n, m = len(graph), edgeSum
print(n, m)

# g = [[0] * (n+1) for _ in range(n+1)]
# g = [[0] * (n+1) for _ in range(n+1)]
g = [[0 for _ in range(n)] for _ in range(n)]
print(g)
        
for i in graph:
    i:Node
    p = i.next
    if p == None:
        continue
    while(1):
        a, b, c = i.head, p.name, p.weight
        print("a : ",a, "b : ", b, "c : ", c)
        g[a][b] = c
        if p.next == None:
            break
        p = p.next

for i in range(0, n):
    for j in range(0, n):
        print(g[i][j], end=' ')
    print()
#여기까진 연결리스트->그래프행렬로변환

# 아래는 그래프행렬에서 이어지지 않은 노드 거리 음의 무한으로 만들기
for i in range(0, n):
    for j in range(0, n):
        if g[i][j] == 0 and (i != j):
            g[i][j]= 999999
        print(g[i][j], end=' ')
    print()


floydWarshall(g)




# 아래는 인접행렬 만드는 함수
                
# *입력 설명

# 첫 번째 줄에는 노드의 수 N(2 ≤ N ≤ 20)과 간선의 수 M이 주어진다.

# 그 다음줄 부터 M줄에 걸쳐 연결정보와 거리비용이 주어진다.

# #input.txt
# 6 9
# 1 2 7
# 1 3 4
# 2 1 2
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5


# *출력 설명
# '''
# 출력 :
# 0 7 4 0 0 0 
# 2 0 5 0 5 0 
# 0 0 0 5 0 0 
# 0 2 0 0 5 0 
# 0 0 0 0 0 0 
# 0 0 0 5 0 0 

# '''
# 가중치 방향그래프를 표현한 인접 행렬을 출력한다.
# import sys
# sys.stdin = open('AA/input_54.txt', 'rt')
# n, m = map(int, input().split())
# g = [[0] * (n+1) for _ in range(n+1)]

# for i in range(m):
#     a, b, c = map(int, input().split())
#     g[a][b] = c

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(g[i][j], end=' ')
#     print()




# 그래프 예제 p.118

# graph = []

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)

# a.addEdge(2, 6)
# a.addEdge(4, 7)
# b.addEdge(3,5)
# b.addEdge(4,8)
# b.addEdge(5,-4)
# c.addEdge(2,-2)
# d.addEdge(3,-3)
# d.addEdge(5,9)
# e.addEdge(1,2)
# e.addEdge(3,7)



# graph.append(a)
# graph.append(b)
# graph.append(c)
# graph.append(d)
# graph.append(e)
