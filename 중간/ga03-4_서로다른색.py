
graph = [
    ['A','B','I','E'],
    ['B','C','G','A'],
    ['C','D','J','B'],
    ['D','E','H','C'],
    ['E','F','A','D'],
    ['F','G','J','E'],
    ['G','H','B','F'],
    ['H','I','D','G'],
    ['I','J','A','H'],
    ['J','C','F','I']
]
intgraph = [
    [0,1,8,4],
    [1,2,6,0],
    [2,3,9,1],
    [3,4,7,2],
    [4,5,0,3],
    [5,6,9,4],
    [6,7,1,5],
    [7,8,3,6],
    [8,9,0,7],
    [9,2,5,8]
]

colorgraph = [0,0,0,0,0,0,0,0,0,0]


colorlist = [1,2,3]

# 순환함수의 역할 
# 1. 상태공간트리 생성
#     각 트리는 1,2,3의 색을 가지는 3가지의 가지로 나누어진다
#     각 계층에서 자신의 부모색과 그래프 리스트의 이웃 노드와 겹치지 않는
#     색을 선택 가능할 때만 아래 계층으로 내려간다.
#     실패시 다시 부모 계층으로 올라가 다른 아래 계층을 진행한다
#     node가 규칙에 맞게 최하위 계층에 도달하면 true를 반환한다

def iscolorOk(node,color):
    if node>0 and colorgraph[node-1] == color:
        return False
    for i in range(1,4):
        if colorgraph[intgraph[node][i]] == color:
            return False
        

    colorgraph[node] = color
    if node == 9:
        return True
    
    for i in range(3):
        if(iscolorOk(node+1, colorlist[i])==True):
            return True


for i in range(1,4):
    if(iscolorOk(0,i)):
        print(colorgraph)
        for i in range(0, 10):
            colorgraph[i] = 0
        print('possible')
        
    

    


    

