# # 3.floyd 알고리즘은 그래프의 모든 노드쌍들간이 최단경로의 길이를 구하는 알고리즘이다.
# # 플로이드 알고리즘이 기반하고 있는 순환식을 기술, 그러한 식이 성립하는 이유

# # 중간에 노드집합 {1,2,...,k}에 속한 노드들만 거쳐서 노
# # 드 i에서 j까지 가는 최단경로는 두가지 경우가 있음: 노드
# # k를 지나는 경우와 지나지 않는 경우

# def FloydWarshall(G):

#     for i in range(0,n):
#         for j in range(0,n):
#             d[i,j] = wij
#             pi[i,j]=None        //최단경로 직전
#     for k in range(0,n):
#         for i in range(0,n):
#             for j in range(0,n):
#                 if d[i,j] > d[i,k] + d[k,j]:
#                     d[i,j] = d[i,k] + d[k,j]
#                     pi[i,j] = k
        
