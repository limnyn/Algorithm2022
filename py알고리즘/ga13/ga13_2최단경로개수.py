# Floyd-Warshall 알고리즘을 응용하여 가중치 방향 그래프의 모든 정점 쌍들간의 최단경로의 “개수”를 구하고자 한다. 
# 그래프의 정점 집합은 V={1,2,...,n}이고, w(u,v)는 정점 u를 v로 연결하는 에지의 가중치이다.
# ck(i,j)는 “정점 i에서 정점 집합 {1,2,...,k}에 속한 정점들 만을 지나서 정점j까지 가는 경로들 중에 최단인 경로의 개수”이다. 
# 모든 정점 쌍들간의 최단경로의 개수를 계산하기 위해서 값 ck(i,j) 에 대한 적절한 순환식을 세워라. 


# 소스 정점 `v`에서 주어진 정점 `u`의 경로를 인쇄하는 재귀 함수
def printPath(path, v, u, route):
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])
 
 
# 최단 비용을 경로로 출력하는 기능
# 모든 정점 쌍 간의 # 정보
def printSolution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                printPath(path, v, u, route)
                route.append(u)
                print(f'The shortest path from {v} —> {u} is', route)
 
 
# Floyd-Warshall 알고리즘을 실행하는 함수
def floydWarshall(adjMatrix):
 
    # 베이스 케이스
    if not adjMatrix:
        return
 
    # `adjMatrix`의 총 정점 수
    n = len(adjMatrix)
 
    # 비용 및 경로 매트릭스는 최단 경로를 저장합니다.
    #(최단 비용/최단 경로) 정보
 
    # 초기에 비용은 가장자리의 무게와 동일합니다.
    cost = adjMatrix.copy()
    path = [[None for x in range(n)] for y in range(n)]
 
    # 초기화 비용 및 경로
    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != 999999:
                path[v][u] = v
            else:
                path[v][u] = -1
 
    # 실행 Floyd-Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # 정점 `k`가 `v`에서 `u`까지의 최단 경로에 있는 경우,
                # 그런 다음 비용[v][u] 및 경로[v][u] 값을 업데이트합니다.
                if cost[v][k] != 999999 and cost[k][u] != 999999 \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
 
            # 대각선 요소가 음수가 되면
            # 그래프에는 음의 가중치 주기가 포함되어 있습니다.
            if cost[v][v] < 0:
                print('Negative-weight cycle found')
                return
 
    # 모든 정점 쌍 사이의 최단 경로를 인쇄합니다.
    printSolution(path, n)
 

if __name__ == '__main__':
 
    #는 무한대를 정의
    I = 999999
 
    # 행렬의 인접 표현이 주어진
    adjMatrix = [
        [0, I, -2, I],
        [4, 0, 3, I],
        [I, I, 0, 2],
        [I, -1, I, 0]
    ]
 
    # Run Floyd–Warshall 알고리즘
    floydWarshall(adjMatrix)