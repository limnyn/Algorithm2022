




import sys
sys.stdin = open('py알고리즘\input.txt', 'rt')
n = 0
total = 0
set=[]

def DFS(L, sum):    #집합의 합이같은부분집합 2개를 찾음

    if sum > total//2:
        return
    if L == n:
        if sum == (total - sum):
            #
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

def DFS1(L, sum, idx,lst):      #1/3합으 찾고 나머지 부분집합을 절반으로 한번더 수행
    global a
    global n
    global total
    sset=lst[:]
    if(idx == 1):
        sset.append(a[L-1])
    if sum > total//3:
        return
    if L == n:
        if(idx == 1):
            sset.append(a[L-1])
        if sum == (total)//3:
            #print("YES1")
            for l in sset:
                a.remove(l)
            # print(sset)    
            # print(a)
            n = len(a)
            total = 0
            for item in a:
                total += item
            #print(n)
            #print(total)
            DFS(0,0)
            
    else:
        DFS1(L+1, sum+a[L],1,sset)
        DFS1(L+1, sum,-1,sset)


if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    total = sum(a)
    vlst=[]
    if(total%3 != 0):
        print("NO")
    else:
        DFS1(0, 0,0,vlst)
        print("NO")

 
    
# 출력 : YES

# 중요내용
# DFS() 함수의 인자 L은 리스트 a의 인덱스 번호를 의미한다.
# DFS() 함수의 인자 sum은 자신이 만든 부분집합 원소의 총합을 의미한다.
# DFS(L+1, sum+a[L]) 코드는 리스트 a의 인덱스 번호가 L인 벨류 값을 부분집합의 원소로 사용하겠다는 의미이다.
# DFS(L+1, sum) 코드는 리스트 a의 인덱스 번호가 L인 벨류 값을 부분집합의 원소로 사용하지 않겠다는 의미이다.
# sys.exit(0)는 해당 코드가 돌아가는 프로그램을 종료시키는 코드이다.
# if sum > total // 2 는 해당 프로그램의 시간 복잡도를 개선하기 위한 코드이다.
# 즉, total을 2로 나눈 몫보다 sum의 값이 커지면 결국 문제에서 원하는 결과(YES)를 얻지 못하기 때문에 나머지 탐색을 할 필요가 없다.
# 따라서 if절의 조건이 sum > total // 2인 경우에는 return을 사용하여 재귀함수(DFS() 함수)를 종료시키고, 불필요한 탐색을 방지하여 시간 복잡도를 개선하는 것이다.
 
# def DFS1(L, sum, idx,lst):
#     sset=lst[:]
#     if(idx == 1):
#         sset.append(a[L-1])
#     if sum > total//2:
#         return
#     if L == n:
#         if(idx == 1):
#             sset.append(a[L-1])
#         if sum == (total-sum):
#             print("YES1")
#             for l in sset:
#                 a.remove(l)
#             print(sset)    
#             print(a)
#             sys.exit(0)
#     else:
#         DFS1(L+1, sum+a[L],1,sset)
#         DFS1(L+1, sum,-1,sset)
